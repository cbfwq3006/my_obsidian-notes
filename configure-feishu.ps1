$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$configScript = Join-Path $repoRoot "scripts\configure_feishu_env.ps1"

Write-Host "This script configures the Feishu bot webhook as Windows user environment variables."
Write-Host "If your Webhook or Secret appeared in a screenshot/chat, regenerate them in Feishu first."
Write-Host ""

$webhookUrl = Read-Host "Enter the new Feishu Webhook URL"
if ([string]::IsNullOrWhiteSpace($webhookUrl)) {
    throw "Webhook URL cannot be empty."
}

$secret = Read-Host "Enter signing Secret, or press Enter if not enabled"

& $configScript -WebhookUrl $webhookUrl -Secret $secret

Write-Host ""
Write-Host "Configured. Test in this PowerShell session with:"
Write-Host ".\test-feishu-push.ps1"
