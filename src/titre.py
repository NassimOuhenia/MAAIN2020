#!/usr/bin/env python
#encoding=utf8
import xml.etree.ElementTree as ET

pref = '{http://www.mediawiki.org/xml/export-0.10/}'

class Titre():
	"""docstring for Titre"""
	def __init__(self, nomFichier):
		super(Titre, self).__init__()
		self.nomFichier = nomFichier
		self.listeTitre=[]
		self.DicoTitre={}

	def generer(self):
		i=0
		tree = ET.ElementTree()
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


def main():
	titre = Titre("/home/andressito/Bureau/M2/semestre2/MAAIN/TP1GH/MAAIN2020/src/wiki_musique.xml")
	titre.generer()
	listeTitre=titre.getListeTitre()
	dicoTitre=titre.getDicoTitre()
	print(listeTitre)
	print(dicoTitre)


if __name__ == "__main__":
	main()
