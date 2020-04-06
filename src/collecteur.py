#!/usr/bin/env python
#encoding=utf8
import xml.etree.ElementTree as ET
from dictionnaire import Dictionnaire
from titre import Titre
import time
import re

fichierMot="../file/listeMotAEnlever"
pref = '{http://www.mediawiki.org/xml/export-0.10/}'
fichierCollecteur='../file/fichierCollecteur.txt'
fichierCorpus=''

class Collecteur():
	"""docstring for Collecteur"""
	def __init__(self, nomFichier,fichierSortie):
		super(Collecteur, self).__init__()
		self.nomFichier = nomFichier
		self.fichierSortie= fichierSortie


	def generer(self, fichier_out):

		dico = Dictionnaire(self.nomFichier,fichierMot)
		print('start cleanning......')
		dico.nettoyage_texte()
		listeMot=dico.getListeMot()
		titre = Titre(self.nomFichier)
		titre.generer()
		dicoTitre=titre.getDicoTitre()
		with open(self.fichierSortie,'w') as fS:
			for mot in listeMot:
				fS.write(mot)
				for event, elem in ET.iterparse(self.nomFichier):
					if elem.tag == pref+'page':
						texte = elem.find(pref+'revision/'+pref+'text').text
						if mot in texte.lower():
							fS.write(";"+str(dicoTitre.get(elem.find(pref+'title').text)))
				fS.write("\n")


def main():
	col= Collecteur(fichierCorpus,
		fichierCollecteur)
	col.generer()
	

if __name__ == "__main__":
	main()
