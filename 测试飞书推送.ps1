$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$notePath = "吃好\2026-05-07 最新菜谱监控.md"
if (-not (Test-Path -LiteralPath $notePath)) {
    throw "找不到测试菜谱文件：$notePath"
}

python scripts/send_feishu_recipe.py $notePath

