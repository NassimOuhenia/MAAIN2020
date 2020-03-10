#!/usr/bin/env python
#encoding=utf8
import xml.etree.ElementTree as ET
file = 'frwikidebut.xml'
racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr">'
mot = 'musique'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
input2='wiki_musique.xml'
input='liste10000Mot.txt'
input3='wiki_musique_cinema_artiste.xml'

def collecteur(name_file):
    i=0
    liste=listeDesMots()
    dic={}
    dicoTitre= avoirDicoTitre()
    for mot in liste:
        if i>50: return dic
        liste=[]
        for event, elem in ET.iterparse(name_file):
            if elem.tag == pref+'page':
                txt = elem.find(pref+'revision/'+pref+'text').text
                if mot in txt:
                    if mot not in dic.keys():
                        liste.append(dicoTitre.get(elem.find(pref+'title').text))
                        dic[mot]=liste
                    else:
                        dic.get(mot).append(dicoTitre.get(elem.find(pref+'title').text))
                #dic=avoirDicoMot(txt,dic,stop_words2)
                # ltee = cleaning2(txt)
                # for i in ltee.split():
                #     if ""
        i+=1
    return dic

def avoirDicoTitre():
    dicoTitre={}
    i=0
    for event, elem in ET.iterparse(input2):
        if elem.tag == pref+'page':
            txt = elem.find(pref+'title').text
            dicoTitre[txt]=i
            i+=1
    return dicoTitre

def listeDesMots():
    res=[]
    for line in open(input, 'r'):
        res.append(line.replace("\n",""))
    return res

def afficher():
    dic=collecteur(input3)
    for cle , val in dic.items():
        print(cle,  val)
print(afficher())
