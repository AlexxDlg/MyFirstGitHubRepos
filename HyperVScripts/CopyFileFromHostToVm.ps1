Get-VM | ft
$VmName = (Get-VM).name
$SourceFile = "C:\ProfWorkFolder\Intune\Get-InstalledSoftware.ps1"
$DestinationPath = "C:\Data\Get-InstalledSoftware.ps1"

$VmName = "vmWin11Hachette"
$SourceFile = Read-host "Enter source file path"
$FileName = Read-Host "Enter the source file name"
$DestinationPath = "C:\Data\$FileName"

Copy-VMFile $VmName -SourcePath $SourceFile -DestinationPath $DestinationPath -CreateFullPath -FileSource Host
