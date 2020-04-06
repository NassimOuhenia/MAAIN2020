
import xml.etree.ElementTree as ET

from matricecreuse import MatriceCreuse as mcreuz
from corpus import Corpus as cpus
from pagerank import PageRank as prank
import time

#écrire titres sur disk
def write_titles(corpus_file, titles_file):

    titles = []
    tree = ET.ElementTree()

    with open(titles_file, 'w') as tout:

        for event, elem in ET.iterparse(corpus_file):
            if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}title':
                tout.write(elem.text+'\n')

    print("END SUCCESS")

#écrire pagerank_sur_disk
def pagerank_sur_disk(file_l, file_c, file_i, e, d, pagerank_out):

    parser = cpus()
    print("start parsing LCI...")
    L, C, I = parser.parse_lci(file_l, file_c, file_i)
    mc = mcreuz(L, C, I)
    pr = prank([1]+[0]*(mc.find_nb_colonne() - 1), mc)
    print("start pagerank_zap...")
    P = pr.pagerank_zap(e, d, pr.Vector)
    print('end pagerank_zap...')

    print('start writing output')
    with open(pagerank_out, 'w') as p_out:
        for p in P:
            p_out.write(str(p)+'\n')
    print('END SUCCESS')

#Tri le collecteur
def tri_collecteur_disk(pagerank_file, collector_file, sorted_collector_file):

    parser = cpus()

    print('start parse pagerank in pageR')
    poids_page = parser.parse_file(pagerank_file, lambda x: float(x))

    print('create pagerank')
    pagerank = prank(poids_page)

    print('start.........sorting')

    with open(collector_file, 'r') as collector, open(sorted_collector_file, 'w') as out:
        for line in collector:

            line = line.split(';')
            pages_sorted = pagerank.tri_pages(line[1:])
            out.write(line[0])

            for id_page, poids in pages_sorted:
                out.write(';'+str(id_page))
            out.write('\n')

    print('END SUCCESS')


if __name__ == "__main__":
'''
    start_time = time.time()
    write_titles("../file/wiki_musique.xml", '../file/titles.txt')
    print("---Temps d execution : " , time.time() - start_time,  "secondes ---")


    pagerank_out = "../file/prank.txt"

    collector_file = "../file/fichier0604.txt"

    sorted_collector_file = "../file/collectorSorted0604.txt"

    file_l = "../file/fileL.txt"
    file_c = "../file/fileC.txt"
    file_i = "../file/fileI.txt"
    parser = cpus()

    d = 0.15
    e = 0.0000001

    start_time = time.time()
    pagerank_sur_disk(file_l, file_c, file_i, e, d, pagerank_out)
    print("---Temps d execution : " , time.time() - start_time,  "secondes ---")

    start_time = time.time()
    tri_collecteur_disk(pagerank_out, collector_file, sorted_collector_file)
    print("---Temps d execution : " , time.time() - start_time,  "secondes ---")
'''
