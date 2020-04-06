#!/usr/bin/env python
#encoding=utf8
import xml.etree.ElementTree as ET
import re
import time
from nltk.corpus import stopwords


pref = '{http://www.mediawiki.org/xml/export-0.10/}'
fichierMotEnlever='../file/listeMotAEnlever'
fichierCorpus='/info/nouveaux/keny/Bureau/M2/MAAIN/Projet/wiki_musique_cinema_artiste.xml'
class Dictionnaire():
    """docstring for Dictionnaire."""

    def __init__(self, name_file,fichierMotAEnlever):
        self.name_file = name_file
        self.fichierMotAEnlever=fichierMotAEnlever
        self.listeMot=[]
        self.dictionnaireListe=[]

    def nettoyage_texte(self):
        dic={}
        stop_wordsFrench = set(stopwords.words('french'))
        for line in open(self.fichierMotAEnlever,'r'):
            for mot in line.split():
                stop_wordsFrench.add(mot)
        numberPage=0
        stop_wordsEnglish = set(stopwords.words('english'))
        for event, elem in ET.iterparse(self.name_file):
            if elem.tag == pref+'page':
                txt = elem.find(pref+'revision/'+pref+'text').text
                txt=formatageTexte(txt)
                dic=avoirDicoMot(txt,dic,stop_wordsFrench,stop_wordsEnglish,numberPage)
                numberPage+=1
                print(numberPage)
        a= sorted(dic.items(), key=lambda x: x[1], reverse = True)
        b=[c for c,d in a ]
        self.dictionnaireListe=a[0:10000]
        self.listeMot=b[0:10000]

    def getListeMot(self):
        return self.listeMot

    def enregisterCollecteur(self,fichierSortie):
        with open(fichierSortie,"w") as fS:
            for elt in self.dictionnaireListe:
                mot,valMot = elt
                _,listePage=valMot
                fS.write(mot)
                for page in listePage:
                    fS.write(";"+str(page))
                fS.write("\n")


def formatageTexte(txt):
    txt = txt.lower()
    txt = re.sub('\s+','  ',txt)
    txt = re.sub('<[^>]+>|\[\[?|\]\]?|\{\{|\}\}|\||:|=+|\W|([0-9]{1,3})', ' ',txt) # les balises
    txt = re.sub(r"'", " ",txt)
    return txt

def avoirDicoMot(txt,dic,stop_wordsFrench,stop_wordsEnglish,numberPage):
    word_tokens=txt.split()
    long= len(word_tokens)
    if long>0 :
        frequence = 1/long
    else : return dic
    aux={}
    for mot in word_tokens:
        if mot not in stop_wordsFrench and mot not in stop_wordsEnglish:
            if mot not in aux.keys():
                aux[mot]=(1,frequence)
            else:
                occ,freq = aux[mot]
                occ+=1
                freq+=frequence
                aux[mot]=(occ,freq)
    aux1={cle:val for cle,val in aux.items() if val[1]>0.005}
    for cle,val in aux1.items():
        occAux,freqAux=val
        if cle in dic.keys():
            occ,listePage=dic[cle]
            occ+=occAux
            listePage.append(numberPage)
            dic[cle]=(occ,listePage)
        else:
            dic[cle]=(occAux,[numberPage])
    return dic

if __name__ == "__main__":
    start_time = time.time()
    dict = Dictionnaire(fichierCorpus,fichierMotEnlever)
    dict.nettoyage_texte()
    print(len(dict.getListeMot()))
    dict.enregisterCollecteur("../file/fichier0604.txt")
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))
