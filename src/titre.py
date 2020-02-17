#!/usr/bin/env python
import xml.etree.ElementTree as ET
import re
import numpy as np

racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr"></mediawiki>'
pref = '{http://www.mediawiki.org/xml/export-0.10/}'


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
            #avoirLien(txt1)
            #return None
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
    liste,dicoTitle=listeTitre(file)
    listeTitreGlobal=listeTitreParPage(file)
    mat=[]
    for i in range(len(liste)):
        mat1=[]
        for j in range(len(liste)):
            if i==j:
                mat1.append(1)
            elif liste[j] in listeTitreGlobal[i]:
                mat1.append(1)
            else :
                mat1.append(0)
        mat.append(mat1)
    print(listeTitreGlobal)
    for i in mat:
        print(i)
    print(len(mat))
