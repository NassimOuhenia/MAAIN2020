
#!/usr/bin/env python3
#encoding=utf8

class MatriceCreuse:

    def __init__(self, L = [0], C = [], I = []):
        self.L = L
        self.C = C
        self.I = I

    #matrice_to_lci
    def matrice_to_lci(self, M):

        step = 0

        for mat1 in M:
            for i in range(len(mat1)):
                if mat1[i] != 0 :
                    step += 1
                    self.C.append(mat1[i])
                    self.I.append(i)
            self.L.append(step)
        return (self.L , self.C, self.I)

    #lci_to_matrice
    def lci_to_matrice(self):
        matrice = []
        lenl = len(self.L)

        for i in range(lenl-1):
            v = [0]*(lenl-1)
            for a in range(self.L[i], self.L[i+1]):
                self.v[I[a]] = self.C[a]
            matrice.append(v)

        return matrice

    #trouver nb colonne à partir de L
    def find_nb_colonne(self):

        return len(self.L) - 1

    #produit LCI x V
    def lci_x_v(self, V):

        result = [0]*len(V)
        lenl = len(self.L)

        for i in range(lenl-1):
            for a in range(self.L[i], self.L[i+1]):
                result[i] += self.C[a]*V[self.I[a]]
        return result

    #produit tM x V
    def trM_x_V(self, V):
        result = [0]*len(V)
        lenl = len(self.L)

        for i in range(lenl-1):
            for a in range(self.L[i], self.L[i+1]):
                result[self.I[a]] += self.C[a]*V[i]
        return result
