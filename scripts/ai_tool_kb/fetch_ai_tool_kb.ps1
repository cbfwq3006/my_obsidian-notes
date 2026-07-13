param(
  [string]$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path,
  [switch]$VerboseLog
)

$ErrorActionPreference = "Continue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

function Get-Sha1([string]$Text) {
  $sha1 = [System.Security.Cryptography.SHA1]::Create()
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
  $hash = $sha1.ComputeHash($bytes)
  return (($hash | ForEach-Object { $_.ToString('x2') }) -join '').Substring(0,10)
}

function Sanitize-FileName([string]$Name) {
  if ([string]::IsNullOrWhiteSpace($Name)) { return "untitled" }
  $invalid = [System.IO.Path]::GetInvalidFileNameChars() -join ''
  $regex = "[$([Regex]::Escape($invalid))]"
  $clean = [Regex]::Replace($Name, $regex, '')
  $clean = [Regex]::Replace($clean, '\s+', ' ').Trim()
  if ($clean.Length -gt 60) { $clean = $clean.Substring(0,60).Trim() }
  return $clean
}

function Clean-Text($Html) {
  if ($Html -is [System.Xml.XmlElement]) { $Html = $Html.InnerText }
  elseif ($Html -and $Html.PSObject.Properties["#text"]) { $Html = $Html."#text" }
  else { $Html = [string]$Html }
  if ([string]::IsNullOrWhiteSpace($Html)) { return "" }
  $text = [Regex]::Replace($Html, '<[^>]+>', ' ')
  $text = [System.Net.WebUtility]::HtmlDecode($text)
  $text = [Regex]::Replace($text, '\s+', ' ').Trim()
  return $text
}

function Parse-DateSafe($Value) {
  if ($null -eq $Value -or [string]::IsNullOrWhiteSpace([string]$Value)) { return $null }
  try { return [DateTime]::Parse([string]$Value) } catch { return $null }
}

function Classify-Item([string]$Title, [string]$Summary, [string]$DefaultCategory) {
  $text = (($Title + " " + $Summary).ToLower())
  if ($text -match 'tutorial|guide|how to|hands-on|cookbook|prompt|workflow|course|learn|build|教程|指南|实操|提示词|工作流') { return '03_教程文章' }
  if ($text -match 'review|benchmark|comparison|compare|versus| vs |best ai tools|tool|app|product hunt|rank|测评|评测|对比|榜单|工具') { return '02_工具测评' }
  if ($text -match 'release|launch|announc|introduc|update|api|model|gpt|claude|gemini|llama|copilot|agent|open source|开源|模型|发布|升级|更新') { return '04_模型产品更新' }
  if ($DefaultCategory) { return $DefaultCategory }
  return '01_行业资讯'
}

function Get-FeedItems($Source) {
  $items = @()
  try {
    $response = Invoke-WebRequest -Uri $Source.url -UseBasicParsing -TimeoutSec 25 -MaximumRedirection 5 -Headers @{ 'User-Agent' = 'Mozilla/5.0 AI Tool KB Bot' }
    [xml]$xml = $response.Content
    if ($xml.rss.channel.item) {
      foreach ($it in $xml.rss.channel.item) {
        $title = Clean-Text (($it.title.InnerText))
        $link = [string]$it.link
        $summary = Clean-Text (($it.description.InnerText))
        if (-not $summary) { $summary = Clean-Text ([string]$it.encoded) }
        $published = Parse-DateSafe $it.pubDate
        $items += [pscustomobject]@{ title=$title; link=$link; summary=$summary; published=$published; source=$Source.name; defaultCategory=$Source.defaultCategory }
      }
    } elseif ($xml.feed.entry) {
      foreach ($it in $xml.feed.entry) {
        $title = Clean-Text (($it.title.InnerText))
        $link = $null
        if ($it.link -is [array]) { $link = ($it.link | Where-Object { $_.href } | Select-Object -First 1).href } elseif ($it.link.href) { $link = $it.link.href } else { $link = [string]$it.link }
        $summary = Clean-Text (($it.summary.InnerText))
        if (-not $summary) { $summary = Clean-Text (($it.content.InnerText)) }
        $published = Parse-DateSafe $it.published
        if (-not $published) { $published = Parse-DateSafe $it.updated }
        $items += [pscustomobject]@{ title=$title; link=$link; summary=$summary; published=$published; source=$Source.name; defaultCategory=$Source.defaultCategory }
      }
    }
  } catch {
    Write-Host "[WARN] fetch failed: $($Source.name) $($Source.url) :: $($_.Exception.Message)"
  }
  return $items
}

$configPath = Join-Path $VaultRoot 'AI工具知识库/99_资料源/sources.json'
$config = Get-Content -LiteralPath $configPath -Raw -Encoding UTF8 | ConvertFrom-Json
$root = Join-Path $VaultRoot 'AI工具知识库'
$since = (Get-Date).AddHours(-1 * [int]$config.fetchWindowHours)
$newCount = 0
$seenCount = 0
$failCount = 0

foreach ($source in $config.sources | Where-Object { $_.enabled -eq $true }) {
  $items = Get-FeedItems $source | Select-Object -First ([int]$config.maxItemsPerSource)
  foreach ($item in $items) {
    if (-not $item.title -or -not $item.link) { continue }
    $pub = $item.published
    if ($pub -and $pub -lt $since) { continue }
    if (-not $pub) { $pub = Get-Date }
    $hash = Get-Sha1 $item.link
    $exists = Get-ChildItem -LiteralPath $root -Recurse -File -Filter "*$hash.md" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($exists) { $seenCount++; continue }

    $category = Classify-Item $item.title $item.summary $item.defaultCategory
    $dir = Join-Path $root $category
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    $dateStr = $pub.ToString('yyyy-MM-dd')
    $fileTitle = Sanitize-FileName $item.title
    $filePath = Join-Path $dir "$dateStr-$fileTitle-$hash.md"
    $summary = $item.summary
    if ($summary.Length -gt 1200) { $summary = $summary.Substring(0,1200) + '……' }
    $created = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

    $md = @"
---
type: ai_tool_item
category: $category
source: "$($item.source)"
url: "$($item.link)"
published: $($pub.ToString('yyyy-MM-dd HH:mm:ss'))
fetched: $created
hash: $hash
status: captured
tags:
  - AI工具知识库
  - $category
---

# $($item.title)

## 来源

- 来源：$($item.source)
- 链接：$($item.link)
- 发布时间：$($pub.ToString('yyyy-MM-dd HH:mm:ss'))
- 分类：$category

## 摘要

$summary

## 待处理

- [ ] 是否值得精读
- [ ] 是否沉淀到 wiki/概念
- [ ] 是否可转为小红书选题

## 我的判断


"@
    Set-Content -LiteralPath $filePath -Value $md -Encoding UTF8
    $newCount++
  }
}

$logPath = Join-Path $root '抓取日志.md'
$line = "`n## $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') 每日抓取`n`n- 新增：$newCount`n- 已存在跳过：$seenCount`n"
Add-Content -LiteralPath $logPath -Value $line -Encoding UTF8
Write-Host "AI工具知识库抓取完成：新增 $newCount，跳过 $seenCount。"

