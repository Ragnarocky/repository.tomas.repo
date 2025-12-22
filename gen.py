import os
import xml.etree.ElementTree as ET
import hashlib

addons = ET.Element('addons')
tree = ET.parse('addon.xml')
addons.append(tree.getroot())
km_tree = ET.parse('zip/kontext_menu/addon.xml')
addons.append(km_tree.getroot())

with open('addons.xml', 'wb') as f:
    f.write(b'<?xml version=""1.0"" encoding=""UTF-8""?>\n')
    f.write(ET.tostring(addons, encoding='utf-8'))

with open('addons.xml', 'rb') as f:
    md5 = hashlib.md5(f.read()).hexdigest()

with open('addons.xml.md5', 'w') as f:
    f.write(md5)

print('MD5: ' + md5)
