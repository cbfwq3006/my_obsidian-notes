$ErrorActionPreference = "Stop"

$signature = @"
using System;
using System.Runtime.InteropServices;

public static class MoveFileExNative {
    [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
    public static extern bool MoveFileEx(string lpExistingFileName, string lpNewFileName, int dwFlags);
}
"@

Add-Type -TypeDefinition $signature

$MOVEFILE_DELAY_UNTIL_REBOOT = 0x4

$paths = @(
    "C:\Program Files (x86)\Kingsoft\WPS Office",
    "D:\PDF"
)

foreach ($root in $paths) {
    if (-not (Test-Path -LiteralPath $root)) {
        continue
    }

    Get-ChildItem -LiteralPath $root -Recurse -Force -File -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        ForEach-Object {
            [MoveFileExNative]::MoveFileEx($_.FullName, $null, $MOVEFILE_DELAY_UNTIL_REBOOT) | Out-Null
            Write-Host "Scheduled file delete on reboot: $($_.FullName)"
        }

    Get-ChildItem -LiteralPath $root -Recurse -Force -Directory -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        ForEach-Object {
            [MoveFileExNative]::MoveFileEx($_.FullName, $null, $MOVEFILE_DELAY_UNTIL_REBOOT) | Out-Null
            Write-Host "Scheduled directory delete on reboot: $($_.FullName)"
        }

    [MoveFileExNative]::MoveFileEx($root, $null, $MOVEFILE_DELAY_UNTIL_REBOOT) | Out-Null
    Write-Host "Scheduled root delete on reboot: $root"
}

