$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
$FetchScript = Join-Path $VaultRoot 'scripts/ai_tool_kb/fetch_ai_tool_kb.ps1'
$WeeklyScript = Join-Path $VaultRoot 'scripts/ai_tool_kb/weekly_review_ai_tool_kb.ps1'

$DailyAction = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$FetchScript`""
$DailyTrigger = New-ScheduledTaskTrigger -Daily -At 8:00AM
Register-ScheduledTask -TaskName 'Obsidian-AI工具知识库-每日抓取' -Action $DailyAction -Trigger $DailyTrigger -Description '每天抓取 AI 工具行业资讯并归档到 Obsidian' -Force | Out-Null

$WeeklyAction = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$WeeklyScript`""
$WeeklyTrigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 8:00PM
Register-ScheduledTask -TaskName 'Obsidian-AI工具知识库-每周复盘' -Action $WeeklyAction -Trigger $WeeklyTrigger -Description '每周生成 AI 工具知识复盘报告' -Force | Out-Null

Write-Host '定时任务已安装：'
Write-Host '- Obsidian-AI工具知识库-每日抓取：每天 08:00'
Write-Host '- Obsidian-AI工具知识库-每周复盘：每周日 20:00'
