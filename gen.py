import os
import glob
import zipfile
import xml.etree.ElementTree as ET
import hashlib


def get_addon_xml_from_zip(zip_path):
    """Načte addon.xml z kořene addonového zipu."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        for name in z.namelist():
            parts = name.split('/')
            # addon.xml je přesně 2 úrovně hluboko: addonid-verze/addon.xml
            if len(parts) == 2 and parts[1] == 'addon.xml':
                return ET.fromstring(z.read(name).decode('utf-8'))
    raise FileNotFoundError(f'addon.xml not found in {zip_path}')


addons = ET.Element('addons')

# 1) Samotný repozitář
repo_tree = ET.parse('addon.xml')
addons.append(repo_tree.getroot())

# 2) kontext_menu
km_tree = ET.parse('zip/kontext_menu/addon.xml')
addons.append(km_tree.getroot())

# 3) plugin.video.tshare – přečteme přímo ze zipu
tshare_zips = sorted(glob.glob('zip/plugin.video.tshare/plugin.video.tshare-*.zip'))
if tshare_zips:
    tshare_xml = get_addon_xml_from_zip(tshare_zips[-1])
    addons.append(tshare_xml)
    print(f'Tshare verze: {tshare_xml.get("version")} ({os.path.basename(tshare_zips[-1])})')
else:
    print('VAROVÁNÍ: nenalezen žádný zip pro plugin.video.tshare')

# Zapíšeme addons.xml
with open('addons.xml', 'wb') as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write(ET.tostring(addons, encoding='utf-8'))

# Spočítáme MD5
with open('addons.xml', 'rb') as f:
    content = f.read()
    md5 = hashlib.md5(content).hexdigest()

with open('addons.xml.md5', 'w') as f:
    f.write(md5)

# Některé starší Kodi verze čtou .md5.txt
with open('addons.xml.md5.txt', 'w') as f:
    f.write(md5)

print(f'addons.xml vygenerován – MD5: {md5}')
