$ErrorActionPreference = "Stop"
Set-StrictMode -Version 3

$VaultRoot = Split-Path -Parent $PSScriptRoot
$Recipient = "cbfwq3006@163.com"
$DraftPath = Join-Path $VaultRoot "weekly-schedule-report-draft.md"
$LogPath = Join-Path $VaultRoot "weekly-schedule-report.log"
$ConfigPath = Join-Path $VaultRoot ".obsidian\weekly-report-email.json"

function Write-ReportLog {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $LogPath -Value "[$timestamp] $Message" -Encoding UTF8
}

function Get-WeekRange {
    param([datetime]$Date)
    $daysSinceMonday = (([int]$Date.DayOfWeek + 6) % 7)
    $start = $Date.Date.AddDays(-$daysSinceMonday)
    $end = $start.AddDays(6)
    [pscustomobject]@{
        Start = $start
        End = $end
    }
}

function ConvertFrom-CodePoints {
    param([int[]]$CodePoints)
    return -join ($CodePoints | ForEach-Object { [char]$_ })
}

function Get-CnPattern {
    $words = @(
        @(0x4F1A,0x8BAE),
        @(0x65E5,0x7A0B),
        @(0x5F85,0x529E),
        @(0x5B89,0x6392),
        @(0x7EA6,0x8C08),
        @(0x6C47,0x62A5),
        @(0x5BA1,0x6838),
        @(0x53F0,0x8D26),
        @(0x660E,0x5929)
    )
    $escapedWords = $words | ForEach-Object { [regex]::Escape((ConvertFrom-CodePoints $_)) }
    return ($escapedWords -join "|")
}

function Get-WeeklyItems {
    param(
        [datetime]$Start,
        [datetime]$End
    )

    $datePatterns = for ($date = $Start; $date -le $End; $date = $date.AddDays(1)) {
        [regex]::Escape($date.ToString("yyyy-MM-dd")),
        [regex]::Escape($date.ToString("yyyyMMdd"))
    }

    $joinedDatePatterns = $datePatterns -join "|"
    $combinedPattern = $joinedDatePatterns + "|" + (Get-CnPattern)
    $items = New-Object System.Collections.Generic.List[string]

    Get-ChildItem -LiteralPath $VaultRoot -Recurse -File -Include "*.md" -ErrorAction SilentlyContinue |
        Where-Object {
            $_.FullName -notmatch "\\\.git\\" -and
            $_.FullName -notmatch "\\\.obsidian\\plugins\\" -and
            $_.FullName -notmatch "\\obsidian.*\\_tools\\"
        } |
        ForEach-Object {
            $file = $_
            $fileIsWeekly = $false
            for ($date = $Start; $date -le $End; $date = $date.AddDays(1)) {
                if ($file.BaseName -eq $date.ToString("yyyyMMdd") -or $file.BaseName -eq $date.ToString("yyyy-MM-dd")) {
                    $fileIsWeekly = $true
                    break
                }
            }

            $lineNumber = 0
            Get-Content -LiteralPath $file.FullName -Encoding UTF8 -ErrorAction SilentlyContinue |
                ForEach-Object {
                    $lineNumber++
                    $line = $_.Trim()
                    if ($line.Length -gt 0 -and ($fileIsWeekly -or $line -match $combinedPattern)) {
                        $relativePath = Resolve-Path -LiteralPath $file.FullName -Relative
                        $items.Add(("{0}:{1} {2}" -f $relativePath, $lineNumber, $line))
                    }
                }
        }

    if ($items.Count -eq 0) {
        return @("No clear schedule items were found in local Obsidian notes this week.")
    }

    return $items | Select-Object -Unique
}

function Get-MailConfig {
    if (Test-Path -LiteralPath $ConfigPath) {
        return Get-Content -LiteralPath $ConfigPath -Encoding UTF8 | ConvertFrom-Json
    }

    $required = @(
        "WEEKLY_REPORT_SMTP_SERVER",
        "WEEKLY_REPORT_SMTP_PORT",
        "WEEKLY_REPORT_SMTP_USER",
        "WEEKLY_REPORT_SMTP_PASSWORD",
        "WEEKLY_REPORT_FROM"
    )

    foreach ($name in $required) {
        if ([string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($name, "User"))) {
            return $null
        }
    }

    [pscustomobject]@{
        smtpServer = [Environment]::GetEnvironmentVariable("WEEKLY_REPORT_SMTP_SERVER", "User")
        smtpPort = [int][Environment]::GetEnvironmentVariable("WEEKLY_REPORT_SMTP_PORT", "User")
        smtpUser = [Environment]::GetEnvironmentVariable("WEEKLY_REPORT_SMTP_USER", "User")
        smtpPassword = [Environment]::GetEnvironmentVariable("WEEKLY_REPORT_SMTP_PASSWORD", "User")
        from = [Environment]::GetEnvironmentVariable("WEEKLY_REPORT_FROM", "User")
        useSsl = $true
    }
}

$week = Get-WeekRange -Date (Get-Date)
$subject = "Weekly schedule report ({0} to {1})" -f $week.Start.ToString("yyyy-MM-dd"), $week.End.ToString("yyyy-MM-dd")
$items = @(Get-WeeklyItems -Start $week.Start -End $week.End)

$bodyLines = @(
    "Weekly schedule report",
    ("Period: {0} to {1}" -f $week.Start.ToString("yyyy-MM-dd"), $week.End.ToString("yyyy-MM-dd")),
    "",
    "Detected schedule items:",
    ""
)

for ($i = 0; $i -lt $items.Count; $i++) {
    $bodyLines += ("{0}. {1}" -f ($i + 1), $items[$i])
}

$bodyLines += @(
    "",
    "Note:",
    "This report is generated from local Obsidian notes. If the Google Calendar plugin is not authenticated, Google Calendar events are not included."
)

$body = $bodyLines -join [Environment]::NewLine
$draft = @(
    "# Weekly Schedule Report Email Draft",
    "",
    "To: $Recipient",
    "",
    "Subject: $subject",
    "",
    "Body:",
    "",
    $body
) -join [Environment]::NewLine

Set-Content -LiteralPath $DraftPath -Value $draft -Encoding UTF8
Write-ReportLog "Draft updated: $DraftPath"

$config = Get-MailConfig
if ($null -eq $config) {
    Write-ReportLog "SMTP config missing; skipped sending email."
    exit 0
}

$securePassword = ConvertTo-SecureString ([string]$config.smtpPassword) -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ([string]$config.smtpUser, $securePassword)

Send-MailMessage `
    -To $Recipient `
    -From ([string]$config.from) `
    -Subject $subject `
    -Body $body `
    -SmtpServer ([string]$config.smtpServer) `
    -Port ([int]$config.smtpPort) `
    -UseSsl:([bool]$config.useSsl) `
    -Credential $credential `
    -Encoding UTF8

Write-ReportLog "Email sent to $Recipient"
