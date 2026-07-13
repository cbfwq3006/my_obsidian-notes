$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
$Pwsh = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$FetchScript = Join-Path $VaultRoot 'scripts\ai_tool_kb\fetch_ai_tool_kb.ps1'
$WeeklyScript = Join-Path $VaultRoot 'scripts\ai_tool_kb\weekly_review_ai_tool_kb.ps1'
$DailyLauncher = Join-Path $VaultRoot 'scripts\ai_tool_kb\daily_fetch.cmd'
$WeeklyLauncher = Join-Path $VaultRoot 'scripts\ai_tool_kb\weekly_review.cmd'
$Schtasks = "$env:SystemRoot\System32\schtasks.exe"

Set-Content -LiteralPath $DailyLauncher -Value "@echo off`r`n`"$Pwsh`" -NoProfile -ExecutionPolicy Bypass -File `"$FetchScript`"`r`n" -Encoding ASCII
Set-Content -LiteralPath $WeeklyLauncher -Value "@echo off`r`n`"$Pwsh`" -NoProfile -ExecutionPolicy Bypass -File `"$WeeklyScript`"`r`n" -Encoding ASCII

& $Schtasks /Create /TN "Obsidian-AI-Tool-KB-Daily-Fetch" /TR "`"$DailyLauncher`"" /SC DAILY /ST 08:00 /F
& $Schtasks /Create /TN "Obsidian-AI-Tool-KB-Weekly-Review" /TR "`"$WeeklyLauncher`"" /SC WEEKLY /D SUN /ST 20:00 /F

Write-Host '定时任务已安装：'
Write-Host '- Obsidian-AI-Tool-KB-Daily-Fetch：每天 08:00'
Write-Host '- Obsidian-AI-Tool-KB-Weekly-Review：每周日 20:00'
