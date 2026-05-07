param(
    [Parameter(Mandatory = $true)]
    [string]$WebhookUrl,

    [Parameter(Mandatory = $false)]
    [string]$Secret = ""
)

if ($WebhookUrl -notmatch '^https://') {
    throw "WebhookUrl should start with https://"
}

[Environment]::SetEnvironmentVariable("FEISHU_WEBHOOK_URL", $WebhookUrl, "User")
$env:FEISHU_WEBHOOK_URL = $WebhookUrl

if ($Secret.Trim().Length -gt 0) {
    [Environment]::SetEnvironmentVariable("FEISHU_WEBHOOK_SECRET", $Secret, "User")
    $env:FEISHU_WEBHOOK_SECRET = $Secret
} else {
    [Environment]::SetEnvironmentVariable("FEISHU_WEBHOOK_SECRET", $null, "User")
    Remove-Item Env:\FEISHU_WEBHOOK_SECRET -ErrorAction SilentlyContinue
}

Write-Host "FEISHU_WEBHOOK_URL configured for current user."
if ($Secret.Trim().Length -gt 0) {
    Write-Host "FEISHU_WEBHOOK_SECRET configured for current user."
} else {
    Write-Host "FEISHU_WEBHOOK_SECRET cleared because no secret was provided."
}
Write-Host "Restart Codex or the automation runner before relying on scheduled runs."

