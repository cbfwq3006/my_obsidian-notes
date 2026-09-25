param(
    [int]$IntervalMinutes = 60
)

$ErrorActionPreference = "Stop"

if ($IntervalMinutes -lt 5) {
    throw "IntervalMinutes must be at least 5."
}

$watcher = Join-Path $PSScriptRoot "watch_obsidian_temp_box.ps1"
$startupFolder = [Environment]::GetFolderPath("Startup")
$launcherName = "Obsidian-TempBox-Watcher.vbs"
$launcherPath = Join-Path $startupFolder $launcherName
$watcherEscaped = $watcher.Replace("""", """""")
$launcher = @"
Set shell = CreateObject("WScript.Shell")
shell.Run "PowerShell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File ""$watcherEscaped"" -IntervalMinutes $IntervalMinutes", 0, False
"@

Set-Content -LiteralPath $launcherPath -Value $launcher -Encoding ASCII

$started = $false
try {
    Start-Process -FilePath "PowerShell.exe" -WindowStyle Hidden -ArgumentList @(
        "-NoProfile"
        "-WindowStyle"
        "Hidden"
        "-ExecutionPolicy"
        "Bypass"
        "-File"
        $watcher
        "-IntervalMinutes"
        $IntervalMinutes
    )
    $started = $true
}
catch {
    Write-Warning "Watcher will start at next user logon because immediate launch was blocked: $($_.Exception.Message)"
}

Write-Output "Installed current-user startup watcher: $launcherPath"
Write-Output "Interval: every $IntervalMinutes minutes"
Write-Output "Watcher: $watcher"
Write-Output "Startup launcher: $launcherPath"
Write-Output "Started now: $started"
