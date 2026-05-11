$script = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "scripts\schedule-wps-remnant-delete.ps1"
Start-Process -FilePath "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" -ArgumentList @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", "`"$script`""
) -Verb RunAs -Wait

