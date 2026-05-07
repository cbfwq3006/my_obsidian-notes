$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$recipeDir = Get-ChildItem -LiteralPath $repoRoot -Directory | Where-Object { $_.Name -eq ([char]21507 + [char]22909) } | Select-Object -First 1
if ($null -eq $recipeDir) {
    throw "Recipe folder not found."
}

$note = Get-ChildItem -LiteralPath $recipeDir.FullName -File |
    Where-Object { $_.Name -like "*最新菜谱监控.md" } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($null -eq $note) {
    throw "Recipe monitor note not found."
}

Write-Host "Sending note:"
Write-Host $note.FullName

python scripts/send_feishu_recipe.py $note.FullName
