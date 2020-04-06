
#!/usr/bin/env python3
#encoding=utf8
import math
from matricecreuse import MatriceCreuse as MC
from corpus import Corpus as CP

class PageRank:

    #+infini
    oo = math.inf

    def __init__(self, Vector = [], mc = MC()):
        self.Vector = Vector
        self.MatriceC = mc

    #distance entre deux Vecteurs
    def distance_V1_V2(self, V1, V2):

        dist = 0
        len_v = len(V1)

        for i in range(len_v):

            dist += (V2[i] - V1[i])**2

        return (dist/len_v)

    #Exo2_1
    def Exo2_1(slef, dep, nb_pas):

        Z = [0]*self.MatriceC.find_nb_colonne()

        Z[dep] = 1

        print('depart', dep)
        print(Z)

        for i in range(nb_pas):
            Z1 = self.MatriceC.trM_x_V(Z)

            print('dist : ', self.distance_V1_V2(Z, Z1))

            print(Z1)
            Z = Z1

    #pagerank_0
    def pagerank_0(self, e):

        Z = [1]+[0]*(self.MatriceC.find_nb_colonne() - 1)

        dist = self.oo

        while (e < dist):

            Z1 = self.MatriceC.trM_x_V(Z)
            dist = self.distance_V1_V2(Z, Z1)
            Z = Z1

        return Z

    #variante_zap
    def variante_zap(self, V, d):

        lenv = len(V)

        result = self.MatriceC.trM_x_V(V)

        for i in range(lenv):
            result[i] = (d/lenv) + (1 - d)*result[i]

        return result

    #pagerank_zap
    def pagerank_zap(self, e, d, Z):

        dist = self.oo

        while (e < dist):

            Z1 = self.variante_zap(Z, d)
            dist = self.distance_V1_V2(Z, Z1)
            Z = Z1

        return Z

    #TRI collecteur by pagerank
    def tri_pages(self, list_page):

        poids_page = [(list_page[i], self.Vector[int(list_page[i])]) for i in range(len(list_page))]

        return sorted(poids_page, key = lambda x: x[1], reverse = True)


"""
if __name__ == "__main__":

    prank = PageRank()
    mc = MC()
    cp = CP()

    M = [[0, 0.5, 0, 0.5],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0.33, 0.33, 0.33, 0]]

    L, C, I = mc.matrice_to_lci(M)

    print(prank.pagerank_zap(0.00000000001, 0.15, [1]+[0]*(prank.MatriceC.find_nb_colonne() - 1)))
"""
