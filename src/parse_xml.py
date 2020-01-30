#!/usr/bin/env python
#encoding=utf8

import xml.etree.ElementTree as ET
import re

file = 'frwikidebut.xml'
mot = 'musique'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
out = 'wiki_musique.xml'

#exo 1
def reduire_mot_cle(name_file, mot_cle, out):

    tree = ET.parse(name_file)
    root = tree.getroot()

    for page in root.findall(pref+'page'):
        txt = page.find(pref+'revision/'+pref+'text').text
        if mot not in txt:
            root.remove(page)
    tree.write(out)

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def cleaning (string):
    #string = re.sub('de$','e',string)
    #string = string.strip('-=')
    string = re.sub('&#233;','e',string)   # è
    string = re.sub('la?e?s?$',' ',string)    # j'ai fait un truc ca ne marche plus
    #string = re.sub('=+',' ',string)     # les =
    string = re.sub('<[^>]+>', '',string) # les balises
    return string

def remove_tags(text):
    return ''.join(ET.fromstring(text).itertext())


def dictionnaire_de_mot(name_file):
    dic={"===":"","le":"","la":"","de":"","un":"","une":"","}}":"",}
    for line in open(name_file,"r"):
        #line=replace_all(line,dic)
        line=cleaning(line)
        #line=remove_tags(line)
        print(line.split())

    return None




def splitfichier(name):
    r=open("out2.xml",'w')
    i=0
    for line in open(name,'r'):
        if i<2383:
            r.write(line)
            i+=1
    return None

#print(reduire_mot_cle("testfichier.xml", "musique", "out.xml"))

#nombres de pages
def count_page(name_file):
    return len(ET.parse(name_file).getroot().findall(pref+'page'))


print(count_page("out.xml"))
print(count_page("testfichier.xml"))
print(dictionnaire_de_mot("out2.xml"))
