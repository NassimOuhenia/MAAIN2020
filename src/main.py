
from corpus import Corpus as cpus
from sEngine import Engine as se
import time

cltr = 'file/collectorSorted0604.txt'
cltr1 = '../file/collectorSorted.txt'
pg = 'file/prank.txt'
ttls = 'file/titles.txt'
lien = 'https://fr.wikipedia.org/wiki/'

def init():

    parser = cpus()

    print('loading collector...')
    collector = parser.parse_collector(cltr)
    print('loading pagerank.....')
    pagerank = parser.parse_file(pg, lambda x: float(x))
    print('loading titles......')
    titles = parser.parse_titles(ttls)

    return se(collector, pagerank), titles


def loop(engine, titles):

    print('search engine start.......')

    while True:

        request = input('$earch? > ')

        start_time = time.time()
        response = engine.generateResponse(request, engine.merge)

        print(len(response)," Résultats : " , time.time() - start_time,  "secondes")

        for id in response[:10]:
            print('\t$ ',lien+engine.genererLink(titles[id]))
        print('\t.')
        print('\t.')
        print('\t.')

def start():
    start_time = time.time()
    search_engine, titles = init()
    print("---Temps d execution : " , time.time() - start_time,  "secondes ---")
    loop(search_engine, titles)


if __name__ == "__main__":
    start()
