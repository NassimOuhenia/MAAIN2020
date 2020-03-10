#!/usr/bin/env python
#encoding=utf8

import xml.etree.ElementTree as ET
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import FrenchStemmer
import nltk
from difflib import SequenceMatcher
#nltk.download('punkt')

file = 'frwikidebut.xml'
racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr">'
mot = 'musique'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
out = 'wiki_musique.xml'
rac='<?xml version="1.0" ?></xml>'
monFichierPetit='wiki_musique.xml'
fichierMot='listeMotAEnlever'
#exo 1


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def cleaning (string):
    string= string.lower()
    string = re.sub('\s+',' ',string)
    string = re.sub('<[^>]+>', ' ',string) # les balises
    string = re.sub('\[*.*?\]', ' ',string) # les balises
    string = re.sub('\{\{.*?\}\}', ' ',string)
    string = re.sub('=+.*?=+', ' ',string)
    string = re.sub('\(*.*?\)', ' ',string)
    string = re.sub('&lt;.*?&gt;', ' ',string)
    string = re.sub(r'https?:\/\/.*[\r\n]*', ' ', string, flags=re.MULTILINE)
    string = re.sub('\*',' ',string)
    string = re.sub('\W',' ',string)
    string = re.sub('\d','',string)
    # string = re.sub('é','e',string)
    # string = re.sub('è','e',string)
    # string = re.sub('ê','e',string)
    # string = re.sub('ë','e',string)
    # string = re.sub('à','a',string)
    # string = re.sub('â','a',string)
    # string = re.sub('ä','a',string)
    # string = re.sub('î','i',string)
    # string = re.sub('ï','i',string)
    # string = re.sub('ç','c',string)
    #string = re.sub('à?â?ä?','a',string)
    #string = re.sub('œ','oe',string)
    #string = re.sub('ô?ö?','o',string)
    #string = re.sub('ù?û?ü?','u',string)
    #ç
    #print(string)
    return string

def avoirTitle(name_file):
    tree = ET.parse(name_file)
    root = tree.getroot()
    title=[]
    i=0
    for page in root.findall(pref+'page'):
        txt = page.find(pref+'title').text
        txt=txt.lower()
        #print(txt)
        #txt=cleaning(txt)
        title.append(txt)
        #for i in txt.split():
            #title.append(i)
    return title

def trouverRacine(mot):
    ps=FrenchStemmer()
    return ps.stem(mot)

def ressemblanceMot(motAChercher,liste):
    ratio=0.8
    resultat=[mot for mot in liste if SequenceMatcher(None, motAChercher, mot).ratio() >= ratio]
    return resultat

def nettoyage(name):
    dic={}
    stop_words = set(stopwords.words('french'))

    #stop_words.add("a")
    #print(sorted(stop_words))
    #ps=PorterStemmer()
    for line in open(name,'r'):
        line =cleaning(line)
        word_tokens = word_tokenize(line)
        #filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                if w not in dic.keys():
                    dic[w]=1
                else: dic[w]+=1
                filtered_sentence.append(w)
                #print(w, " : ", ps.stem(w))
        #print(filtered_sentence)
    a = sorted(dic.items(), key=lambda x: x[1])
    b=[c for c,d in a ]
    #print(b)
    return a

def essayerTouverMot():
    liste=nettoyage("outfevrier.xml")
    while True:
        mot = input("Entrez un mot à rechercher : ")
        print(" le mot qui se rapproche le plus est: ", ressemblanceMot(mot,liste))

def cleaning2(txt):
    txt=txt.lower()
    txt = re.sub('\s+','  ',txt)
    txt = re.sub('<[^>]+>', ' ',txt) # les balises
    #txt = re.sub('\[\[[^\]]+\]\]', ' ',txt)
    #txt = re.sub('\{\{[^\}]+\}\}', ' ',txt)
    txt = re.sub('\[\[?', ' ',txt)
    txt = re.sub('\]\]?', ' ',txt)
    txt = re.sub('\{\{', ' ',txt)
    txt = re.sub('\}\}', ' ',txt)
    txt = re.sub('\|', ' ',txt)
    txt = re.sub(':', ' ',txt)
    txt = re.sub('=+', ' ',txt)
    txt = re.sub(r"'", " ",txt)
    txt = re.sub('\W',' ',txt)
    txt = re.sub('([0-9]{1,3})',' ',txt)
    #txt = re.sub('\[*.*?\]', '',txt)
    #txt = re.sub('\{\{.*?\}\}', ' ',txt)
    #txt = re.sub('\{*.*?\}', ' ',txt)
    return txt

def nettoyage_methode_nassim(name_file):
    dic={}
    stop_words = set(stopwords.words('french'))
    for line in open(fichierMot,'r'):
        for m in line.split():
            stop_words.add(m)
    stop2 = set(stopwords.words('english'))
    for event, elem in ET.iterparse(name_file):
        if elem.tag == pref+'page':
            txt = elem.find(pref+'revision/'+pref+'text').text
            txt=cleaning2(txt)
            dic=avoirDicoMot(txt,dic,stop_words,stop2)
            #dic=avoirDicoMot(txt,dic,stop_words2)
            # ltee = cleaning2(txt)
            # for i in ltee.split():
            #     if ""
    a = sorted(dic.items(), key=lambda x: x[1], reverse = True)
    b=[c for c,d in a ]
    c=b[0:10000]
    enregistrerMot(c)
    return c

def enregistrerMot(liste):
    f=open("liste10000Mot.txt","w")
    for i in liste:
        f.write(i+"\n")
    f.close()

def avoirDicoMot(txt,dic,stop_words,stop2):

    word_tokens = word_tokenize(txt)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words :
            if w not in stop2:
                if w not in dic.keys():
                    dic[w]=1
                else: dic[w]+=1
                filtered_sentence.append(w)
    return dic

#print(testReduire())
#print(essayerTouverMot())
#print(avoirTitle(monFichierPetit))
#print(ouvrir2efile())
#print(nettoyage(monFichierPetit))
nettoyage_methode_nassim(monFichierPetit)
