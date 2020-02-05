#!/usr/bin/env python
#encoding=utf8

import xml.etree.ElementTree as ET
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
#nltk.download('punkt')

file = 'frwikidebut.xml'
mot = 'musique'
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
        txt= txt.lower()
        music=0
        for mot in mots:
            if mot in txt:
                music+=1
        if music ==0:
            root.remove(page)
    tree.write(out,encoding="utf-8", xml_declaration=None, default_namespace=None, method="xml")
    print("ok")

def testReduire():
    mots3=["infobox musique"]
    print(reduire_mot_cle2("/home/andressito/Bureau/M2/semestre2/MAAIN/TP1/frwiki.xml",mots3,"outputFinal.xml"))

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
    string = re.sub('\W',' ',string)
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
        line =cleaning(line)
        word_tokens = word_tokenize(line)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        print(filtered_sentence)
    return None

#print(testReduire())
print(nettoyage("outfevrier.xml"))
#print(ouvrir2efile())
