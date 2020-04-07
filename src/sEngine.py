
from corpus import Corpus as cpus
import re

class Engine:

    def __init__(self, collector = {}, pagerank = []):
        self.collector = collector
        self.pagerank = pagerank

    #1 mot clé return ids pages
    def first_word(self, mot_cle):

        if mot_cle in self.collector.keys():
            return self.collector[mot_cle]
        else:
            return []

    #intersection
    def intersect(self, v1, v2):
        result = []
        i = 0
        j = 0

        while i < len(v1) and j < len(v2):
            if v1[i] == v2[j]:
                result.append(v1[i]) #ajout titre page #i
                i += 1
                j += 1
            elif v1[i] < v2[j]:
                i += 1
            else:
                j += 1

        return result

    #fusion
    def merge(self, v1, v2):
        result = []
        i = 0
        j = 0
        lenv1 = len(v1)
        lenv2 = len(v2)

        while i < lenv1 and j < lenv2:

            rank_v1i = self.pagerank[v1[i]]#poids page id #i
            rank_v2j = self.pagerank[v2[j]]#poids page id #j

            if rank_v1i == rank_v2j:
                result.append(v1[i])
                if v1[i] != v2[j]:
                    result.append(v2[j])
                i += 1
                j += 1
            elif rank_v2j < rank_v1i:
                result.append(v1[i])
                i += 1
            else:
                result.append(v2[j])
                j += 1

        if i < lenv1:
            result += v1[i:]
        elif j < lenv2:
            result += v2[j:]

        return result

    #response
    def generateResponse(self, request, f): #f option merge ou intersection

        response = []

        for mot in request.split():
            response = f(response, self.first_word(mot.lower()))

        return response

    #lien
    def genererLink(self, title):
        return re.sub('\s+', '_', title)
