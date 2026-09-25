#requires -Version 5.1
<#
.SYNOPSIS
  obsidian-cc — Windows OCR helper (Windows.Media.Ocr / WinRT)

.DESCRIPTION
  On-device OCR: no dependencies, no network, no API key. Called by the plugin's
  agent-bridge "vision gate" when the configured model does NOT accept images —
  it turns a raw/ screenshot into text so the agent can still digest it.

  powershell.exe -NoProfile -ExecutionPolicy Bypass -File ocr.ps1 -Path <image>

  Prints nothing (exit 0) when no text is recognized; the plugin then falls back
  to its "image skipped" notice. Exits nonzero on errors.

.NOTES
  Requires Windows 10/11. For Chinese, install a Chinese (zh-Hans-CN / zh-TW)
  language pack (Settings > Time & Language > Language). The Windows OCR engine
  is single-language per engine, so this prefers a zh-* recognizer when present,
  else en-*, else the user's profile languages. Mixed CJK+Latin in one image is
  therefore weaker than macOS Vision (which handles multi-language natively); if
  that matters on Windows, RapidOCR is the accuracy upgrade.

  UNTESTED on real Windows yet — authored from the documented OcrEngine pattern.
  The plugin degrades gracefully: any failure here returns empty stdout and the
  agent gets the "image skipped" notice instead. Please validate on a Windows box.
#>
param([Parameter(Mandatory = $true)][string]$Path)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Path)) {
    [Console]::Error.WriteLine("error: file not found: $Path")
    exit 1
}

# --- WinRT projection bootstrap ----------------------------------------------
Add-Type -AssemblyName System.Runtime.WindowsRuntime

# Generic awaiter for WinRT IAsyncOperation<T> — PowerShell has no `await`.
$awaitMethod = [System.WindowsRuntimeSystemExtensions].GetMethods() |
    Where-Object {
        $_.Name -eq 'AsTask' -and
        $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.FullName -eq 'Windows.Foundation.IAsyncOperation`1'
    } | Select-Object -First 1

function Await($op, $resultType) {
    $m = $awaitMethod.MakeGenericMethod($resultType)
    $t = $m.Invoke($null, @($op))
    $t.Wait(-1) | Out-Null
    $t.Result
}

# Force-load the WinRT types we reference (so MakeGenericMethod / casts resolve).
[Windows.Storage.StorageFile,             Windows.Storage,          ContentType=WindowsRuntime] > $null
[Windows.Graphics.Imaging.BitmapDecoder,  Windows.Graphics.Imaging, ContentType=WindowsRuntime] > $null
[Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime] > $null
[Windows.Media.Ocr.OcrEngine,             Windows.Media.Ocr,        ContentType=WindowsRuntime] > $null

try {
    $file    = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($Path)) ([Windows.Storage.StorageFile])
    $stream  = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    # Bgra8 is the pixel format the OCR engine expects.
    $bitmap  = Await ($decoder.GetSoftwareBitmapAsync(
                        [Windows.Graphics.Imaging.BitmapPixelFormat]::Bgra8,
                        [Windows.Graphics.Imaging.BitmapAlphaMode]::Premultiplied)) `
                     ([Windows.Graphics.Imaging.SoftwareBitmap])

    # Prefer a Chinese recognizer, then English, then the user's profile default.
    $langs = [Windows.Media.Ocr.OcrEngine]::AvailableRecognizerLanguages
    $preferred = $langs | Where-Object { $_.LanguageTag -like 'zh*' } | Select-Object -First 1
    if (-not $preferred) {
        $preferred = $langs | Where-Object { $_.LanguageTag -like 'en*' } | Select-Object -First 1
    }
    $engine = if ($preferred) {
        [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($preferred)
    } else {
        [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
    }
    if (-not $engine) {
        [Console]::Error.WriteLine("error: no OCR language available. Install a language pack (Settings > Time & Language).")
        exit 1
    }

    $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $text = $result.Text
    if ($text) { Write-Output $text.Trim() }
    exit 0
} catch {
    [Console]::Error.WriteLine("error: OCR failed: $($_.Exception.Message)")
    exit 1
}
