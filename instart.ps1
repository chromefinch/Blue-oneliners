$users = Get-ChildItem -Path "C:\Users" -Name
foreach ($user in $users) {
$locations= "C:\Users\"+$user+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
$files = Get-ChildItem -Path $locations -Name -ErrorAction SilentlyContinue
if ($files -ne $null){
foreach ($file in $files){ 
Write-Host $locations"\"  -NoNewline
Write-Host $file -ForegroundColor Red }}
else{foreach ($location in $locations) {
Write-Host $location"\"}
}}
