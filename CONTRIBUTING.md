# Přispívání do repozitáře

Děkujeme za zájem o přispění do tohoto repozitáře!

## 🔧 Jak aktualizovat doplňky

### 1. Přidání nového doplňku
- Umístěte ZIP soubor do složky `zip/nazev-doplnku/`
- Aktualizujte soubor `addons.xml` s novými informacemi
- Přepočítejte MD5 hash: `Get-FileHash -Algorithm MD5 addons.xml`
- Aktualizujte `addons.xml.md5.txt` s novým hashem

### 2. Aktualizace existujícího doplňku
- Nahraďte ZIP soubor v příslušné složce
- Zvyšte číslo verze v `addons.xml`
- Přepočítejte a aktualizujte MD5 hash

### 3. Kontrolní seznam před commitem
- [ ] Nový/aktualizovaný ZIP soubor je ve správné složce
- [ ] Verze v `addons.xml` je správná
- [ ] MD5 hash je přepočítán a aktualizován
- [ ] Funkčnost byla otestována v Kodi

## 📝 Formát commit zpráv
- `feat: přidán nový plugin XYZ v1.0.0`
- `fix: oprava chyby v plugin ABC`
- `chore: aktualizace MD5 hashů`

## 🛠️ Užitečné příkazy

### Přepočítání MD5 (PowerShell)
```powershell
Get-FileHash -Algorithm MD5 addons.xml | Select-Object -ExpandProperty Hash
```

### Vytvoření ZIP archivu doplňku
```powershell
Compress-Archive -Path plugin-folder/* -DestinationPath zip/plugin-name/plugin-name-version.zip
```