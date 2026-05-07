$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$configScript = Join-Path $repoRoot "scripts\configure_feishu_env.ps1"

Write-Host "此脚本会把飞书机器人 Webhook 配置到 Windows 当前用户环境变量。"
Write-Host "如果 Webhook 或 Secret 曾经出现在截图/聊天里，请先到飞书重新生成后再继续。"
Write-Host ""

$webhookUrl = Read-Host "请输入新的飞书 Webhook URL"
if ([string]::IsNullOrWhiteSpace($webhookUrl)) {
    throw "Webhook URL 不能为空。"
}

$secret = Read-Host "请输入签名 Secret（没开启签名校验可直接回车）"

& $configScript -WebhookUrl $webhookUrl -Secret $secret

Write-Host ""
Write-Host "配置完成。当前 PowerShell 会话可直接测试："
Write-Host "python scripts/send_feishu_recipe.py `"吃好\2026-05-07 最新菜谱监控.md`""

