#!/usr/bin/env python
#encoding=utf8

import xml.etree.ElementTree as ET

file = 'frwikidebut.xml'
mot = 'musique'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
out = 'wiki_musique.fr'

#exo 1
def reduire_mot_cle(name_file, mot_cle, out):

    tree = ET.parse(name_file)
    root = tree.getroot()

    for page in root.findall(pref+'page'):
        txt = page.find(pref+'revision/'+pref+'text').text
        if mot not in txt:
            root.remove(page)
    tree.write(out)

#reduire_mot_cle(file, mot, out)

#nombres de pages
def count_page(name_file):

    return len(ET.parse(name_file).getroot().findall(pref+'page'))


#print(count_page(out))
