$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$notePath = "吃好\2026-05-07 最新菜谱监控.md"
if (-not (Test-Path -LiteralPath $notePath)) {
    throw "Recipe note not found: $notePath"
}

python scripts/send_feishu_recipe.py $notePath
