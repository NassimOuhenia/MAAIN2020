
#!/usr/bin/env python3
#encoding=utf8

import xml.etree.ElementTree as ET

class Corpus:

    RACINE = '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="fr">'
    PREF = '{http://www.mediawiki.org/xml/export-0.10/}'
    NBPAGE = 200000

    def __init__(self, name_file = None, key_words = ['musique', 'cinéma', 'artiste'], out_file = "wiki_musique.xml"):
        self.name_file = name_file
        self.key_words = key_words
        self.out_file = out_file

    #parse_file_to_list
    def parse_file(self, file, f):

        lines = open(file, 'r').readlines()

        for index in range(len(lines)):
            lines[index] = f(lines[index])

        return lines

    #parse_lci_files_to_lists
    def parse_lci(self, file_l, file_c, file_i):

        l = self.parse_file(file_l, lambda x : int(x))
        c = self.parse_file(file_c, lambda x : float(x))
        i = self.parse_file(file_i, lambda x : int(x))

        return l, c, i

    #parse_collector_file_to_dict
    def parse_collector(self, collector_file):

        collector = {}

        with open(collector_file, 'r') as c:
            for line in c:

                line = line.split(';')
                pages = line[1:]

                for i in range(len(pages)):
                    pages[i] = int(pages[i])

                collector[line[0]] = pages

        return collector

    #parse_titres_to_liste
    def parse_titles(self, titles_file):

        return open(titles_file, 'r').readlines()

    #reduction_frwiki_to_corpus_of_NBPAGE
    def reduction(self):
        i = 0
        with open(self.out_file, 'w') as o:
            o.write(self.RACINE)
            for event, elem in ET.iterparse(self.name_file):
                if elem.tag == self.PREF+'page':
                    txt = elem.find(self.PREF+'revision/'+self.PREF+'text').text
                    if txt:
                        for mot in self.key_words:
                            if 'infobox '+mot in txt.lower():
                                elemstr = ET.tostring(elem, encoding="unicode", method="xml")
                                o.write(elemstr)
                                i += 1
                                print(i)

                                #s'arreter à NBPAGE pages
                                if i == self.NBPAGE:
                                    break

            o.write('</mediawiki>')
            print('SUCCESS')

'''
if __name__ == "__main__":
    cpus = Corpus("/info/master2/Public/MAAIN2020/frwiki-20200120-pages-meta-current.xml")
    cpus.reduction()
'''
