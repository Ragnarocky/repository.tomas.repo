# Tomas Kodi Repository

Oficiální repozitář Kodi doplňků od Tomase obsahující pokročilé pluginy pro streamování obsahu.

## 📦 Obsažené doplňky

### [Tshare Plugin](zip/plugin.video.tshare/) (v0.6.0)
Pokročilý Kodi plugin pro přehrávání obsahu ze služby Webshare.cz

**Hlavní funkce:**
- 🔍 Inteligentní vyhledávání obsahu na Webshare
- 📺 Přehrávání filmů a seriálů
- 📋 Správa front a historie přehrávání  
- 💾 Možnost stahování souborů
- 🎯 TMDB integrace pro metadata a plakáty

### [Kontext Menu](zip/kontext_menu/) (v1.0.0) 
Rozšíření kontextové nabídky pro rychlé akce s obsahem

## 🚀 Instalace

1. **Stažení repozitáře:**
   - Stáhněte soubor `repository.tomas.repo-1.0.0.zip` z [releases](../../releases)
   - Nebo použijte přímý odkaz: `https://github.com/Ragnarocky/repository.tomas.repo/raw/main/repository.tomas.repo-1.0.0.zip`

2. **Instalace do Kodi:**
   - Otevřete Kodi → Doplňky → Instalovat ze ZIP souboru
   - Vyberte stažený ZIP soubor
   - Repozitář se objeví v seznamu repozitářů

3. **Instalace pluginů:**
   - Přejděte na Doplňky → Instalovat z repozitáře → Tomas Repository
   - Vyberte požadovaný plugin a klikněte na "Instalovat"

## 📋 Požadavky

- **Kodi verze:** 21.0+ (Omega)
- **Python:** 3.0.1+
- **Dodatečné moduly:** `script.module.unidecode`

## 🔗 Přímé odkazy

- **Repository XML:** `https://raw.githubusercontent.com/Ragnarocky/repository.tomas.repo/main/addons.xml`
- **Download složka:** `https://raw.githubusercontent.com/Ragnarocky/repository.tomas.repo/main/zip/`

### Nové funkce ve verzi 0.5.0
- sloučen addon s kontextovým menu do jednoho balíčku
- automatická instalace TMDB Helper player konfigurace při prvním spuštění
- přímé vyhledávání bez keyboard dialogu z TMDB Helper
- robustní error handling a caching pro lepší výkon
- detailní logování pro debugging
- opraveny syntax warningy
- vylepšené parsování TMDB formátu

### Klíčové opravy a vylepšení z 15.9.2025

#### 🐛 **Kritické opravy**
- **Oprava vyhledávání seriálů** - vyřešen problém, kdy SeriesManager nebyl správně volán
- **Filtrování seriálů vs. filmy** - vyhledávání seriálů už nevyhazuje epizody při hledání filmů
- **Epizodové vyhledávání** - opravena detekce různých formátů epizod (S1E6 ↔ S01E06)
- **URL parsing s ampersandy** - vyřešeny problémy se speciálními znaky v názvech filmů
- **TMDB API integrace** - stabilnější načítání metadat z The Movie Database

#### 🎯 **Nové funkce**
- **Flexibilní vyhledávání epizod** - zadáš `seriál S1E6` a najde všechny formáty
- **Chytré vyhledávací strategie** - různé přístupy pro filmy, seriály a epizody
- **Episode search mode** - speciální logika pro přímé hledání konkrétních dílů
- **Vylepšená relevance** - přesnější filtrování irelevantních výsledků
- **Unicode normalizace** - lepší podpora diakritiky v názvech

#### 🔍 **Algoritmy vyhledávání**
- **Inteligentní detekce obsahu** - automaticky rozpozná, zda hledáš film, seriál nebo epizodu
- **Pokročilé regex vzory** - podporuje S01E01, S1E6, 1x06, E06, Episode 6 atd.
- **Fallback mechanismy** - pokud selže jedna metoda, zkusí jinou
- **Cache optimalizace** - rychlejší opakované vyhledávání
- **Year-aware matching** - zohledňuje rok vydání při řazení výsledků

#### 📊 **Vylepšení výkonu**
- **Optimalizované API volání** - méně dotazů na server díky chytrému cachování
- **Progresivní vyhledávání** - postupně načítá výsledky podle priority
- **Memory management** - lepší správa dočasných dat a cache
- **Error resilience** - robustnější zpracování chyb síťového připojení

#### 🎬 **Správce obsahu**
- **Historie přehrávání** - rozdělen na filmy a seriály s kompletními metadaty
- **Mazání z historie** - možnost odstranit konkrétní položky
- **TMDB plakáty** - automatické načítání posterů filmů
- **Seriálové pokračování** - sledování pokroku v jednotlivých seriálech

#### 🛠️ **Developer improvements**
- **Lepší logování** - detailnější debug informace pro řešení problémů
- **Modulární kód** - čistší architektura pro snadnější údržbu
- **Error handling** - comprehensive exception handling ve všech funkcích
- **Code documentation** - více komentářů a vysvětlení logiky

### Nejnovější vylepšení (září 2024)

#### 🎯 **Inteligentní vyhledávání a řazení**
- **Chytrý algoritmus vyhledávání** - využívá TMDB metadata pro přesnější výsledky
- **Inteligentní řazení souborů** podle kvality (4K, 1080p, 720p), jazyka (český dabing priorita) a velikosti
- **Deduplikace výsledků** - automaticky odstraní duplicitní soubory, zachová nejlepší verzi
- **Pokročilé filtrování** - vyřazuje irelevantní výsledky podle shody názvů a roků
- **Cache systém** - rychlejší opakované vyhledávání díky inteligentnímu cachování

#### 📺 **Vylepšený správce seriálů**
- **Automatická detekce epizod** - rozpoznává formáty S01E01, 1x01, E01 atd.
- **Chytré řazení streamů** - preferuje české dabingy a vyšší kvality
- **Hledání chybějících dílů** - automaticky dohledá chybějící epizody
- **Flexibilní výběr streamů** - možnost zvolit alternativní stream pro konkrétní díl
- **Historie přehrávání seriálů** - sleduje pokrok v jednotlivých seriálech

#### 🎬 **Historie přehrávání filmů**
- **Kompletní metadata** - ukládá plakáty, popisy a TMDB informace
- **Rychlé opakované přehrání** - přímý přístup k už jednou přehrávaným filmům
- **TMDB integrace** - automatické načítání informací o filmech
- **Snadná správa** - možnost mazání položek z historie

#### 🔍 **Pokročilé vyhledávání epizod**
- **Flexibilní formáty** - podporuje S1E6, S01E06, 1x06, E06 a další
- **Inteligentní matching** - správně páruje různé formáty epizod
- **Přesné výsledky** - místo 6 náhodných výsledků najde skutečné epizody
- **Bezfiltrové vyhledávání** - možnost "Hledat bez filtrů" pro pokročilé uživatele

#### ⚡ **Výkonnostní optimalizace**
- **Rychlejší vyhledávání** - optimalizované API volání s caching
- **Paměťová efektivita** - lepší správa cache a dočasných dat
- **Robustní error handling** - lepší zpracování chyb a fallbacky
- **Detailní logování** - pro snadnější debugging a podporu

#### 🎨 **Uživatelské rozhraní**
- **Kontextová menu** - rychlé akce přímo z výsledků vyhledávání
- **Progress dialogy** - vizuální feedback při delších operacích
- **Informativní notifikace** - jasné zprávy o stavu operací
- **Konzistentní ikony** - jednotný vzhled napříč funkcemi

#### 🔧 **Technické vylepšení**
- **Modulární architektura** - čistší kód a lepší udržovatelnost
- **Vylepšené regex vzory** - přesnější detekce epizod a formátů
- **Unicode normalizace** - lepší podpora diakritiky a speciálních znaků
- **Bezpečné URL handling** - správné zpracování speciálních znaků v názvech

## Použití

1. Stáhněte a nainstalujte doplněk ze zip souboru
2. Nakonfigurujte svoje přihlašovací údaje v nastavení doplňku
3. **Konfigurace TMDB Helper playeru:**
   - Otevřete TMDB Helper
   - Jděte do **Nastavení → Players → Configure players**
   - Klikněte na **"Create new player"**
   - Vyberte **Tshare** ze seznamu
   - JSON soubor se automaticky nainstaluje
   - Ukončete konfiguraci tlačítkem **"Zpět"**
4. **Ověření funkčnosti:**
   - Restartujte Kodi (doporučeno)
   - V TMDB Helper najděte film nebo díl požadovaného seriálu. Po odkliknutí se spustí automatické vyhledávání.
   - Použijte kontextové menu (pravé tlačítko). Kde můžete vyhledat celý seriál.
  5. **Přímé použití pluginu:**
   - Alternativně můžete plugin spustit přímo z **Doplňky → Video**
   - Najděte **"Tshare"** a spusťte

## Instalace doplňku

### Instalace z repozitáře GitHub

Existuje několik způsobů, jak nainstalovat tento doplněk přímo z GitHubu:

#### Metoda 1: Stažení a instalace z ZIP souboru

1. Stáhněte si ZIP soubor tohoto repozitáře:

   - Klikněte na tlačítko "Code" na hlavní stránce repozitáře
   - Vyberte "Download ZIP"
   - Stáhne se soubor s celým repozitářem
     
2. V Kodi:
   
   - Jděte do "Nastavení" (ikona ozubeného kola)
   - Vyberte "Doplňky"
   - Klikněte na "Instalovat z archivu ZIP"
   - Najděte stažený ZIP soubor
   - Počkejte na oznámení o úspěšné instalaci

#### Metoda 2: Pomocí GitHub Browser doplňku

1. Nainstalujte doplněk "GitHub Browser" z oficiálního repozitáře Kodi
2. Spusťte GitHub Browser
3. Vyhledejte "plugin.video.Tshare" nebo URL tohoto repozitáře
4. Vyberte tento doplněk a klikněte na "Instalovat"

#### Poznámka:

Pro správné fungování je potřeba mít platný účet Webshare a být přihlášen v nastavení doplňku.

## Varování

Plugin neposkytuje žádný obsah, je to jen simulace prohlížeče veřejně dostupné webové stránky.

Nejsem zodpovědný za obsah, který tato stránka poskytuje.
