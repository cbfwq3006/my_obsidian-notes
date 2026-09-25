param(
    [int]$IntervalMinutes = 60,
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = "Continue"

function From-CodePoint {
    param([int[]]$CodePoints)
    return (($CodePoints | ForEach-Object { [char]$_ }) -join "")
}

if ($IntervalMinutes -lt 5) {
    $IntervalMinutes = 5
}

$scanner = Join-Path $PSScriptRoot "scan_obsidian_temp_box.ps1"
$logName = (From-CodePoint @(0x0030, 0x0030, 0x4E34, 0x65F6, 0x7BB1, 0x81EA, 0x52A8, 0x5DE1, 0x68C0)) + ".log"
$logPath = Join-Path $Root ("projects\" + $logName)
$mutex = New-Object System.Threading.Mutex($false, "Local\ObsidianTempBoxWatcher")

try {
    if (-not $mutex.WaitOne(0)) {
        exit 0
    }
}
catch {
    exit 1
}

try {
    while ($true) {
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -LiteralPath $logPath -Value "[$timestamp] scan-start" -Encoding UTF8

        try {
            & $scanner *>> $logPath
            Add-Content -LiteralPath $logPath -Value "[$timestamp] scan-end exit=$LASTEXITCODE" -Encoding UTF8
        }
        catch {
            Add-Content -LiteralPath $logPath -Value "[$timestamp] scan-error $($_.Exception.Message)" -Encoding UTF8
        }

        Start-Sleep -Seconds ($IntervalMinutes * 60)
    }
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
}
