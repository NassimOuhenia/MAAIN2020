#!/usr/bin/env python
import xml.etree.ElementTree as ET
import re
import numpy as np

racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr"></mediawiki>'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
monFichierPetit='wiki_musique.xml'

def listeTitre(file):
    title=[]
    dicoTitle={}
    i=0
    tree = ET.ElementTree()
    root = ET.fromstring(racine)
    for event, elem in ET.iterparse(file):
        if elem.tag == pref+'page':
            txt = elem.find(pref+'title').text
            title.append(txt)
            dicoTitle[txt]=i
            i+=1
            txt1=elem.find(pref+'revision/'+pref+'text').text
    return (title,dicoTitle)

def listeTitreParPage(file):
    title,dicoTitle=listeTitre(file)
    return avoirLien(file,title)

def avoirLien(file,listeTitle):
    res=[]
    tree = ET.ElementTree()
    root = ET.fromstring(racine)
    for event, elem in ET.iterparse(file):
        if elem.tag == pref+'page':
            res1=[]
            txt = elem.find(pref+'revision/'+pref+'text').text
            m = re.findall(r'\[\[(.*?)\]\]',txt) # les balises
            for mot in m:
                if mot in listeTitle and mot not in res1 : res1.append(mot)
            res.append(res1)
    return res

def matriceTitle(file):
    #I indice du ie
    #C valeur du truc
    liste,dicoTitle=listeTitre(file)
    listeTitreGlobal=listeTitreParPage(file)
    L=[]
    C=[]
    I=[]
    mat=[]
    L.append(0)
    k=0
    for i in range(len(liste)):
        mat1=[]
        a=0
        for j in range(len(liste)):
            if liste[j] in listeTitreGlobal[i]:
                I.append(dicoTitle[liste[j]])
                a+=1
                k+=1
        L.append(k)
        if a>0:
            for b in range(a):
                C.append(1/a)
    #print(listeTitreGlobal)
    print('L ',L)
    print('C ',C)
    print('I ',I)

def matriceTitle2(file):
    liste,dicoTitle=listeTitre(file)
    L=[]
    C=[]
    I=[]
    mat=[]
    L.append(0)
    k=0
    for event, elem in ET.iterparse(file):
        if elem.tag == pref+'page':
            res1=[]
            txt = elem.find(pref+'revision/'+pref+'text').text
            m = re.findall(r'\[\[(.*?)\]\]',txt) # les balises
            for mot in m:
                if mot in liste and mot not in res1 : res1.append(mot)
            a=0
            for j in range(len(liste)):
                if liste[j] in res1:
                    I.append(dicoTitle[liste[j]])
                    a+=1
                    k+=1
            L.append(k)
            if a>0:
                for b in range(a):
                    C.append(1/a)
    print('L ',L)
    print('C ',C)
    print('I ',I)
#print(listeTitre(monFichierPetit))
#matriceTitle(monFichierPetit)
#print(listeTitreParPage(monFichierPetit))
print(matriceTitle(monFichierPetit))
print(matriceTitle2(monFichierPetit))
