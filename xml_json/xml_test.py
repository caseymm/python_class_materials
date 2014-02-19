import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

print root
print root.tag
print root.attrib

print root[0][1].text

for child in root:
    print child.attrib['name']

for n in root.iter('neighbor'):
    print n.attrib
    
for n in root[2].iter('neighbor'):
    print n.attrib
    
#for child in root:
#    print child.tag, child.attrib