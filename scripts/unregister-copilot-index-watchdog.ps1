$ErrorActionPreference = "Stop"
Set-StrictMode -Version 3

$TaskName = "CopilotIndexWatchdog"

& reg.exe DELETE "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v $TaskName /f | Out-Null

$running = Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like "*copilot-index-watchdog.ps1* -Loop*" }

foreach ($proc in $running) {
    Stop-Process -Id $proc.ProcessId -Force -ErrorAction SilentlyContinue
}

if ($running) {
    Write-Host "Auto-start entry removed and watchdog process stopped: $TaskName"
} else {
    Write-Host "Auto-start entry removed: $TaskName"
}
