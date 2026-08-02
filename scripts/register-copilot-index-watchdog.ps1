$ErrorActionPreference = "Stop"
Set-StrictMode -Version 3

$TaskName = "CopilotIndexWatchdog"
$ScriptPath = Join-Path $PSScriptRoot "copilot-index-watchdog.ps1"

if (-not (Test-Path -LiteralPath $ScriptPath)) {
    throw "Watchdog script not found: $ScriptPath"
}

$runCommand = "powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$ScriptPath`" -Loop"

& reg.exe ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v $TaskName /t REG_SZ /d $runCommand /f | Out-Null
Write-Host "Auto-start registry entry registered: $TaskName"
Write-Host "It will run after the next Windows logon."
