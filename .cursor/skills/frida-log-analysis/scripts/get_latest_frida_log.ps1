param(
    [string]$Directory = "C:\FRIDA\TuringExpo\Local\3129455\Logs",
    [int]$Tail = 0,
    [switch]$IncludeContent
)

if (-not (Test-Path -LiteralPath $Directory)) {
    Write-Error "Directory not found: $Directory"
    exit 1
}

$latest = Get-ChildItem -LiteralPath $Directory -Filter '*.txt' -File |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if (-not $latest) {
    Write-Error "No .txt log files found in $Directory"
    exit 1
}

if ($IncludeContent.IsPresent) {
    $tailLines = @()
    if ($Tail -gt 0) {
        $tailLines = Get-Content -LiteralPath $latest.FullName -Tail $Tail
    }

    $obj = [PSCustomObject]@{
        path         = $latest.FullName
        lastWriteTime = $latest.LastWriteTime
        tailLines    = $tailLines
    }

    $obj | ConvertTo-Json -Depth 3
} else {
    $latest.FullName
}

