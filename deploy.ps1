# Deployment Helper Script
# Spusťte tento skript po aktualizaci addons.xml

Write-Host "🔄 Aktualizace repozitáře..." -ForegroundColor Yellow

# 1. Přepočítání MD5 hash
Write-Host "📊 Přepočítávám MD5 hash..." -ForegroundColor Blue
$md5Hash = (Get-FileHash -Algorithm MD5 addons.xml).Hash.ToLower()
$md5Hash | Out-File -FilePath "addons.xml.md5.txt" -Encoding utf8 -NoNewline

Write-Host "✅ Nový MD5 hash: $md5Hash" -ForegroundColor Green

# 2. Vytvoření nového ZIP archivu repozitáře
Write-Host "📦 Vytvářím ZIP archiv repozitáře..." -ForegroundColor Blue
$version = "1.0.0"  # Aktualizujte podle potřeby
$zipName = "repository.tomas.repo-$version.zip"

if (Test-Path $zipName) {
    Remove-Item $zipName
}

Compress-Archive -Path addon.xml,icon.png,fanart.jpg -DestinationPath $zipName -Force
Write-Host "✅ Vytvořen $zipName" -ForegroundColor Green

# 3. Ověření struktury
Write-Host "🔍 Ověřuji strukturu..." -ForegroundColor Blue

# Zkontrolovat XML syntax (pokud je dostupný xmllint)
try {
    [xml]$xmlContent = Get-Content addons.xml
    Write-Host "✅ addons.xml má platnou XML syntaxi" -ForegroundColor Green
} catch {
    Write-Host "❌ Chyba v addons.xml syntaxi!" -ForegroundColor Red
    exit 1
}

# Zkontrolovat existence ZIP souborů
$addons = $xmlContent.addons.addon
foreach ($addon in $addons) {
    $addonId = $addon.id
    $version = $addon.version
    $zipPath = "zip\$addonId\$addonId-$version.zip"
    
    if (Test-Path $zipPath) {
        Write-Host "✅ Nalezen $zipPath" -ForegroundColor Green
    } else {
        Write-Host "❌ Chybí $zipPath" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🎉 Repozitář je připraven k nahrání na GitHub!" -ForegroundColor Cyan
Write-Host "Nezapomeňte:"
Write-Host "  1. Commitnout všechny změny"
Write-Host "  2. Pushnout na GitHub"
Write-Host "  3. Vytvořit nový release s $zipName" -ForegroundColor Yellow