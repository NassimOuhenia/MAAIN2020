#!/usr/bin/env python3
#encoding=utf8

import xml.etree.ElementTree as ET
import re

#nltk.download('punkt')

racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr">'
gros = "frwiki.xml"
file = 'frwikidebut.xml'
mot = ['musique', 'cinéma', 'artiste']
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
out = 'wiki_musique.xml'

#exo 1

def reduire_mot_cle(name_file, mots, out):

    tree = ET.parse(name_file)
    root = tree.getroot()
    music=0
    i=0

    for page in root.findall(pref+'page'):

        txt = page.find(pref+'revision/'+pref+'text').text
        txt = txt.lower()
        music = 0

        for mot in mots:
            if mot in txt:
                music += 1

        if music == 0:
            root.remove(page)

    tree.write(out,encoding="utf-8", xml_declaration=None, default_namespace=None, method="xml")

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def cleaning (string):
    string= string.lower()
    string = re.sub('\s+',' ',string)
    string = re.sub('<[^>]+>', '',string) # les balises
    string = re.sub('\[*.*?\]', '',string) # les balises
    string = re.sub('\{\{.*?\}\}', '',string)
    string = re.sub('=+.*?=+', '',string)
    string = re.sub('\(*.*?\)', '',string)
    string = re.sub('&lt;.*?&gt;', '',string)
    string = re.sub(r'https?:\/\/.*[\r\n]*', '', string, flags=re.MULTILINE)
    string = re.sub('\*',' ',string)
    string = re.sub('\W','',string)
    #print(string)
    return string

def remove_tags(text):
    return ''.join(ET.fromstring(text).itertext())

def ouvrir2efile():
    tree = ET.parse("outfevrier.xml")
    root = tree.getroot()
    for page in root.findall(pref+'page'):
        txt = page.find(pref+'revision/'+pref+'text').text
        print(cleaning(txt))
    print("ok")

def nettoyage(name):
    stop_words = set(stopwords.words('french'))
    print(stop_words)
    for line in open(name,'r'):
        line = cleaning(line)
        word_tokens = word_tokenize(line)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        print(filtered_sentence)
    return None

#print(testReduire())
#print(nettoyage("outfevrier.xml"))
#print(ouvrir2efile())

def reduction(name_file, out, mot_cle):

    i = 0
    with open(out, 'w') as o:
        o.write(racine)
        for event, elem in ET.iterparse(name_file):
            if elem.tag == pref+'page':
                txt = elem.find(pref+'revision/'+pref+'text').text
                if txt:
                    for mot in mot_cle:
                        if 'infobox '+mot in txt.lower():
                            elemstr = ET.tostring(elem, encoding="unicode", method="xml")
                            o.write(elemstr)
                            i += 1
                            print(i)
                            if i == 200000:
                                break

        o.write('</mediawiki>')
        print('SUCCESS')

reduction(gros, out, mot)
