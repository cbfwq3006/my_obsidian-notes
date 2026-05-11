$ErrorActionPreference = "Continue"

Write-Host "WPS/Kingsoft cleanup started."

$serviceName = "wpscloudsvr"
$svc = Get-Service -Name $serviceName -ErrorAction SilentlyContinue
if ($null -ne $svc) {
    if ($svc.Status -ne "Stopped") {
        Stop-Service -Name $serviceName -Force -ErrorAction SilentlyContinue
    }
    & "$env:SystemRoot\System32\sc.exe" delete $serviceName | Out-Host
}

$pathsToRemove = @(
    "C:\Program Files (x86)\Kingsoft\WPS Office",
    "C:\Program Files (x86)\Kingsoft\office6",
    "C:\Program Files (x86)\Kingsoft\pdf",
    "D:\PDF"
)

$startMenu = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
Get-ChildItem -LiteralPath $startMenu -Filter "WPS*.lnk" -ErrorAction SilentlyContinue |
    Remove-Item -Force -ErrorAction SilentlyContinue

$shellDlls = @(
    "C:\Program Files (x86)\Kingsoft\WPS Office\12.1.0.24657\office6\kwpsshellext64.dll_d_20767f4_d_2078b8a",
    "C:\Program Files (x86)\Kingsoft\WPS Office\12.1.0.24657\office6\qingshellext64.dll_d_2076823_d_2078b99",
    "D:\PDF\12.8.0.18917\office6\kwpspdfshellext64.dll_d_2145056_d_2145920"
)

foreach ($dll in $shellDlls) {
    if (Test-Path -LiteralPath $dll) {
        & "$env:SystemRoot\System32\regsvr32.exe" /u /s $dll
    }
}

foreach ($path in $pathsToRemove) {
    if (Test-Path -LiteralPath $path) {
        Write-Host "Removing: $path"
        Remove-Item -LiteralPath $path -Recurse -Force -ErrorAction SilentlyContinue
        if (Test-Path -LiteralPath $path) {
            Write-Host "Still exists: $path"
        } else {
            Write-Host "Removed: $path"
        }
    }
}

$kingsoftRoot = "C:\Program Files (x86)\Kingsoft"
if (Test-Path -LiteralPath $kingsoftRoot) {
    $remaining = Get-ChildItem -Force -LiteralPath $kingsoftRoot -ErrorAction SilentlyContinue
    if ($null -eq $remaining) {
        Remove-Item -LiteralPath $kingsoftRoot -Force -ErrorAction SilentlyContinue
    } else {
        Write-Host "Kingsoft root still has non-WPS items; keeping: $kingsoftRoot"
        $remaining | ForEach-Object { Write-Host "  - $($_.Name)" }
    }
}

Write-Host "WPS/Kingsoft cleanup finished."
