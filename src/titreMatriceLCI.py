#!/usr/bin/env python
#encoding=utf8
import xml.etree.ElementTree as ET
from titre import Titre
import re

pref = '{http://www.mediawiki.org/xml/export-0.10/}'

class TitreMatriceLCI(object):
	"""docstring for TitreMatriceLCI"""
	def __init__(self, nomFichier):
		super(TitreMatriceLCI, self).__init__()
		self.nomFichier = nomFichier
		self.fichierL='fichierL.txt'
		self.fichierC='fichierC.txt'
		self.fichierI='fichierI.txt'


	def generer(self):
		titre = Titre(self.nomFichier)
		titre.generer()
		listeTitre=titre.getListeTitre()
		dicoTitre=titre.getDicoTitre()
		print(dicoTitre)
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
	titreMat = TitreMatriceLCI("/home/andressito/Bureau/M2/semestre2/MAAIN/TP1GH/MAAIN2020/src/wiki_musique.xml")
	titreMat.generer()

if __name__ == "__main__":
	main()