param(
  [string]$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path,
  [int]$Days = 7
)

function Get-FrontValue([string]$Text, [string]$Key) {
  $pattern = "(?m)^" + [Regex]::Escape($Key) + ":\s*(.+?)\s*$"
  $m = [Regex]::Match($Text, $pattern)
  if ($m.Success) { return $m.Groups[1].Value.Trim('"') }
  return ""
}

$root = Join-Path $VaultRoot 'AI工具知识库'
$since = (Get-Date).AddDays(-1 * $Days)
$items = @()
$folders = @('01_行业资讯','02_工具测评','03_教程文章','04_模型产品更新')
foreach ($folder in $folders) {
  $dir = Join-Path $root $folder
  if (-not (Test-Path -LiteralPath $dir)) { continue }
  Get-ChildItem -LiteralPath $dir -File -Filter '*.md' | Where-Object { $_.LastWriteTime -ge $since } | ForEach-Object {
    $txt = Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8
    $titleMatch = [Regex]::Match($txt, '(?m)^#\s+(.+)$')
    $title = if ($titleMatch.Success) { $titleMatch.Groups[1].Value.Trim() } else { $_.BaseName }
    $relPath = $_.FullName.Substring($VaultRoot.Length + 1).Replace('\','/')
    $items += [pscustomobject]@{
      Title = $title
      Category = $folder
      Source = Get-FrontValue $txt 'source'
      Url = Get-FrontValue $txt 'url'
      Published = Get-FrontValue $txt 'published'
      Path = $relPath
    }
  }
}

$reportDir = Join-Path $root '06_每周复盘'
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$start = $since.ToString('yyyy-MM-dd')
$end = (Get-Date).ToString('yyyy-MM-dd')
$reportPath = Join-Path $reportDir "$end-AI工具知识周复盘.md"

$groups = $items | Group-Object Category
$total = $items.Count
$topSources = $items | Group-Object Source | Sort-Object Count -Descending | Select-Object -First 5

$keywords = @{
  'Agent/智能体' = 'agent|agents|智能体|代理'
  '模型升级' = 'model|gpt|claude|gemini|llama|模型'
  '编程工具' = 'code|coding|developer|github|copilot|编程|代码'
  '视频/多模态' = 'video|image|multimodal|vision|audio|视频|图像|多模态|语音'
  '企业应用' = 'enterprise|business|work|office|microsoft|企业|办公'
  '开源' = 'open source|opensource|开源'
}
$trendLines = @()
foreach ($k in $keywords.Keys) {
  $count = ($items | Where-Object { ($_.Title.ToLower()) -match $keywords[$k] }).Count
  if ($count -gt 0) { $trendLines += "- $k：$count 条相关内容" }
}
if ($trendLines.Count -eq 0) { $trendLines += "- 本周样本较少，暂不提炼稳定趋势。" }

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add('---')
$lines.Add('type: weekly_review')
$lines.Add("created: $end")
$lines.Add("updated: $end")
$lines.Add('tags:')
$lines.Add('  - AI工具知识库')
$lines.Add('  - 周复盘')
$lines.Add('---')
$lines.Add('')
$lines.Add("# AI工具知识周复盘（$start 至 $end）")
$lines.Add('')
$lines.Add('## 一、本周概览')
$lines.Add('')
$lines.Add("- 收录条目：$total 条")
$lines.Add("- 覆盖分类：$($groups.Count) 类")
$lines.Add('')
$lines.Add('## 二、分类统计')
$lines.Add('')
$lines.Add('| 分类 | 数量 |')
$lines.Add('| --- | ---: |')
foreach ($g in $groups) { $lines.Add("| $($g.Name) | $($g.Count) |") }
$lines.Add('')
$lines.Add('## 三、重点来源')
$lines.Add('')
foreach ($s in $topSources) { $lines.Add("- $($s.Name)：$($s.Count) 条") }
$lines.Add('')
$lines.Add('## 四、趋势信号')
$lines.Add('')
foreach ($line in $trendLines) { $lines.Add($line) }
$lines.Add('')
$lines.Add('## 五、值得精读的条目')
$lines.Add('')
foreach ($item in ($items | Sort-Object Published -Descending | Select-Object -First 20)) {
  $linkPath = $item.Path.Replace('.md','')
  $lines.Add("- [[$linkPath|$($item.Title)]]（$($item.Category) / $($item.Source)）")
}
$lines.Add('')
$lines.Add('## 六、我的复盘')
$lines.Add('')
$lines.Add('### 1. 本周最值得关注的变化')
$lines.Add('')
$lines.Add('')
$lines.Add('### 2. 对我的工作/内容创作有什么启发')
$lines.Add('')
$lines.Add('')
$lines.Add('### 3. 可以转成小红书的选题')
$lines.Add('')
$lines.Add('- ')
$lines.Add('- ')
$lines.Add('- ')
$lines.Add('')
$lines.Add('### 4. 下周重点关注')
$lines.Add('')
$lines.Add('- ')
$lines.Add('- ')
$lines.Add('- ')
$lines.Add('')
$lines.Add('## 七、交给 Codex 深度提炼的提示词')
$lines.Add('')
$lines.Add('```text')
$lines.Add('请基于本周 AI工具知识库的条目，帮我提炼：')
$lines.Add('1. 本周 AI 工具行业的3个核心趋势；')
$lines.Add('2. 值得关注的5个工具/产品；')
$lines.Add('3. 可转成小红书的10个选题；')
$lines.Add('4. 我应该重点跟进的3个方向。')
$lines.Add('要求：简短、具体、不要空话。')
$lines.Add('```')

Set-Content -LiteralPath $reportPath -Value ($lines -join "`n") -Encoding UTF8
Write-Host "周复盘已生成：$reportPath"
