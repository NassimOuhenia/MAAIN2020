#!/usr/bin/env python
#encoding=utf8

import xml.etree.ElementTree as ET
import re
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
racine = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr"></mediawiki>'

class Generer:
	"""docstring for Generer"""
	def __init__(self, nomFichier):
		self.nomFichier = nomFichier

	def genererTitre(self):
		self.listeTitre=[]
		self.DicoTitre={}
		i=0
		tree = ET.ElementTree()
		root = ET.fromstring(racine)
		for event, elem in ET.iterparse(self.nomFichier):
			if elem.tag == pref+'title':
				titreTexte = elem.text
				self.listeTitre.append(titreTexte)
				self.DicoTitre[titreTexte]=i
				i+=1

	def getListeTitre(self):
		return self.listeTitre

	def getDicoTitre(self):
		return self.DicoTitre

	def genererCLI(self):
		self.fichierL='fichierL.txt'
		self.fichierC='fichierC.txt'
		self.fichierI='fichierI.txt'
		self.genererTitre()
		listeTitre=self.getListeTitre()
		dicoTitre=self.getDicoTitre()
		with open(self.fichierL,'w') as fL, open(self.fichierC,'w') as fC, open (self.fichierI,'w') as fI:
			fL.write(str(0)+"\n")
			k=0
			for event, elem in ET.iterparse(self.nomFichier):
				if elem.tag == pref+'page':
					lienExternePage=[]
					texte = elem.find(pref+'revision/'+pref+'text').text
					liens=re.findall(r'\[\[(.*?)\]\]',texte)
					for lien in liens:
						if lien in listeTitre and lien not in lienExternePage:
							lienExternePage.append(lien)
					nombreLiens=0
					for i in range(len(listeTitre)):
						if listeTitre[i] in lienExternePage:
							fI.write(str(dicoTitre[listeTitre[i]])+"\n")
							print(dicoTitre[listeTitre[i]])
							nombreLiens+=1
							k+=1
					fL.write(str(k)+"\n")
					if nombreLiens>0:
						for nb in range(nombreLiens):
							fC.write(str(1/nombreLiens)+"\n")

def main():
    gen = Generer("wiki_musique.xml")
    gen.genererTitre()
    print(gen.getDicoTitre())
    print(gen.getListeTitre())
    print(gen.genererCLI())

if name == 'main':
    main()
