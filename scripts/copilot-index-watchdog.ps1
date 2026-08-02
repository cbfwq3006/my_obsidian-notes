param(
    [switch]$Loop,
    [string]$ConfigPath = (Join-Path $PSScriptRoot "copilot-index-watchdog.config.json")
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version 3

$VaultRoot = Split-Path -Parent $PSScriptRoot
$RuntimeRoot = Join-Path $env:LOCALAPPDATA "sl_obsidian\copilot-watchdog"
$LogPath = Join-Path $RuntimeRoot "watchdog.log"
$StatePath = Join-Path $RuntimeRoot "state.json"

New-Item -ItemType Directory -Force -Path $RuntimeRoot | Out-Null

function Write-Log {
    param([string]$Message)
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $LogPath -Value "[$stamp] $Message" -Encoding UTF8
}

function Get-DefaultConfig {
    [pscustomobject]@{
        checkIntervalMinutes = 15
        staleSlackMinutes = 30
        recentIndexWindowMinutes = 20
        requiredConsecutiveStaleChecks = 2
        cooldownHours = 6
        reindexCommandName = "Force Reindex Vault"
        settingsMenuName = "Advanced Settings"
        obsidianExeCandidates = @(
            "C:\Program Files\Obsidian\Obsidian.exe",
            "C:\Program Files (x86)\Obsidian\Obsidian.exe"
        )
    }
}

function Get-Config {
    if (Test-Path -LiteralPath $ConfigPath) {
        try {
            return Get-Content -LiteralPath $ConfigPath -Encoding UTF8 -Raw | ConvertFrom-Json
        } catch {
            Write-Log "Config parse failed, falling back to defaults: $($_.Exception.Message)"
        }
    }
    return Get-DefaultConfig
}

function Get-State {
    if (Test-Path -LiteralPath $StatePath) {
        try {
            return Get-Content -LiteralPath $StatePath -Encoding UTF8 -Raw | ConvertFrom-Json
        } catch {
            Write-Log "State parse failed, resetting state: $($_.Exception.Message)"
        }
    }
    [pscustomobject]@{
        staleCount = 0
        lastAutoReindexAt = $null
        lastCheckAt = $null
        lastHealthyAt = $null
    }
}

function Save-State {
    param([object]$State)
    $json = $State | ConvertTo-Json -Depth 8
    Set-Content -LiteralPath $StatePath -Value $json -Encoding UTF8
}

function Get-LatestMarkdownFile {
    Get-ChildItem -LiteralPath $VaultRoot -Recurse -File -Filter *.md -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -notmatch '\\\.obsidian\\' } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
}

function Get-LatestCopilotIndexFile {
    $obsidianFolder = Join-Path $VaultRoot ".obsidian"
    if (-not (Test-Path -LiteralPath $obsidianFolder)) {
        return $null
    }

    Get-ChildItem -LiteralPath $obsidianFolder -File -Filter "copilot-index-*.json" -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notlike "*.bak*" } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
}

function Get-ObsidianProcess {
    Get-Process Obsidian -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowHandle -ne 0 } |
        Select-Object -First 1
}

function Get-ObsidianExePath {
    param($Config)

    foreach ($candidate in @($Config.obsidianExeCandidates)) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) {
            return $candidate
        }
    }

    return $null
}

function Trigger-CopilotForceReindex {
    param($Config)

    $proc = Get-ObsidianProcess
    if (-not $proc) {
        $exe = Get-ObsidianExePath -Config $Config
        if (-not $exe) {
            Write-Log "Obsidian not running and executable not found. Skipped reindex trigger."
            return $false
        }

        Write-Log "Obsidian not running. Starting it from: $exe"
        # Open the intended vault directly; launching Obsidian.exe without a
        # vault argument shows the vault picker and interrupts normal work.
        Start-Process -FilePath $exe -ArgumentList "obsidian://open?vault=sl_obsidian" -WindowStyle Hidden | Out-Null
        Start-Sleep -Seconds 8
        $proc = Get-ObsidianProcess
        if (-not $proc) {
            Write-Log "Obsidian failed to create a main window after launch."
            return $false
        }
    }

    Add-Type -AssemblyName UIAutomationClient,UIAutomationTypes

    $handle = [IntPtr]$proc.MainWindowHandle
    $window = [System.Windows.Automation.AutomationElement]::FromHandle($handle)
    if (-not $window) {
        Write-Log "Failed to obtain UIAutomation window from Obsidian handle."
        return $false
    }

    $signature = @"
using System;
using System.Runtime.InteropServices;
public static class WatchdogWin32 {
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")]
    public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
}
"@
    if (-not ("WatchdogWin32" -as [type])) {
        Add-Type -TypeDefinition $signature
    }
    [WatchdogWin32]::ShowWindowAsync($handle, 9) | Out-Null
    Start-Sleep -Milliseconds 400
    [WatchdogWin32]::SetForegroundWindow($handle) | Out-Null
    Start-Sleep -Milliseconds 600

    $settingsButton = $window.FindFirst(
        [System.Windows.Automation.TreeScope]::Descendants,
        (New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::NameProperty,
            [string]$Config.settingsMenuName
        ))
    )

    if (-not $settingsButton) {
        Write-Log "Could not find settings menu '$($Config.settingsMenuName)'."
        return $false
    }

    $expandPattern = $settingsButton.GetCurrentPattern([System.Windows.Automation.ExpandCollapsePattern]::Pattern)
    $expandPattern.Expand()
    Start-Sleep -Milliseconds 500

    $reindexItem = $window.FindFirst(
        [System.Windows.Automation.TreeScope]::Descendants,
        (New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::NameProperty,
            [string]$Config.reindexCommandName
        ))
    )

    if (-not $reindexItem) {
        Write-Log "Could not find menu item '$($Config.reindexCommandName)'."
        return $false
    }

    $invokePattern = $reindexItem.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
    $invokePattern.Invoke()
    Write-Log "Triggered Copilot command: $($Config.reindexCommandName)"
    return $true
}

function Invoke-CheckOnce {
    $config = Get-Config
    $state = Get-State
    $now = Get-Date
    $latestMd = Get-LatestMarkdownFile
    $indexFile = Get-LatestCopilotIndexFile

    $state.lastCheckAt = $now

    if (-not $latestMd) {
        Write-Log "No markdown files found in vault. Skipped."
        Save-State -State $state
        return
    }

    if (-not $indexFile) {
        $stale = $true
        $reason = "missing index"
    } else {
        $indexAgeMinutes = ($now - $indexFile.LastWriteTime).TotalMinutes
        $latestVsIndexMinutes = ($latestMd.LastWriteTime - $indexFile.LastWriteTime).TotalMinutes

        $stale = $latestVsIndexMinutes -gt [double]$config.staleSlackMinutes
        $reason = "latest md is newer than index by {0:N1} minutes" -f $latestVsIndexMinutes

        if ($indexAgeMinutes -lt [double]$config.recentIndexWindowMinutes) {
            $stale = $false
            $reason = "index was updated {0:N1} minutes ago; treating as active" -f $indexAgeMinutes
        }
    }

    if (-not $stale) {
        if ($state.staleCount -ne 0) {
            $state.staleCount = 0
        }
        $state.lastHealthyAt = $now
        Save-State -State $state
        Write-Log ("Healthy. latestMd={0} index={1}" -f $latestMd.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss"), ($(if ($indexFile) { $indexFile.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss") } else { "missing" })))
        return
    }

    $state.staleCount = [int]$state.staleCount + 1
    Write-Log ("Stale check {0}/{1}: {2}" -f $state.staleCount, [int]$config.requiredConsecutiveStaleChecks, $reason)

    $cooldownMinutes = [int]$config.cooldownHours * 60
    if ($state.lastAutoReindexAt) {
        $lastAuto = [datetime]$state.lastAutoReindexAt
        $minutesSinceLastAuto = ($now - $lastAuto).TotalMinutes
        if ($minutesSinceLastAuto -lt $cooldownMinutes) {
            Save-State -State $state
            Write-Log ("Cooldown active ({0:N1} minutes since last auto reindex). Skipped." -f $minutesSinceLastAuto)
            return
        }
    }

    if ($state.staleCount -lt [int]$config.requiredConsecutiveStaleChecks) {
        Save-State -State $state
        return
    }

    $triggered = Trigger-CopilotForceReindex -Config $config
    if ($triggered) {
        $state.lastAutoReindexAt = $now
        $state.staleCount = 0
        Save-State -State $state
        return
    }

    Save-State -State $state
}

$mutex = [System.Threading.Mutex]::new($false, "Local\sl_obsidian_copilot_watchdog")
if (-not $mutex.WaitOne(0)) {
    Write-Log "Another watchdog instance is already running."
    exit 0
}

try {
    Write-Log "Watchdog started. Loop=$Loop Script=$PSCommandPath"
    if ($Loop) {
        $config = Get-Config
        while ($true) {
            try {
                Invoke-CheckOnce
            } catch {
                Write-Log "Check failed: $($_.Exception.Message)"
            }
            Start-Sleep -Seconds ([int]$config.checkIntervalMinutes * 60)
        }
    } else {
        Invoke-CheckOnce
    }
} finally {
    try { $mutex.ReleaseMutex() | Out-Null } catch {}
    $mutex.Dispose()
}
