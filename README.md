$users = Get-ChildItem -Path "C:\\Users" -Name
foreach ($user in $users) {
$here= "C:\\Users"+$user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
$file = Get-ChildItem -Path $here -Name -ErrorAction SilentlyContinue
Write-Host $here""  -NoNewline
Write-Host $file -ForegroundColor Red }

$users = Get-ChildItem -Path "C:\\Users" -Name
foreach ($user in $users) {
$here= "C:\\Users"+$user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
$files = Get-ChildItem -Path $here -Name -ErrorAction SilentlyContinue
foreach ($file in $files) {
Write-Host $here""  -NoNewline
Write-Host $file -ForegroundColor Red }}


\------------Finial Version------------

$users = Get-ChildItem -Path "C:\\Users" -Name
foreach ($user in $users) {
$locations= "C:\\Users"+$user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
$files = Get-ChildItem -Path $locations -Name -ErrorAction SilentlyContinue
if ($files -ne $null){
foreach ($file in $files){
Write-Host $locations""  -NoNewline
Write-Host $file -ForegroundColor Red }}
else{foreach ($location in $locations) {
Write-Host $location""}
}}

