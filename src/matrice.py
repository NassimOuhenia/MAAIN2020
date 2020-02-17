#!/usr/bin/env python

class Matrice:
    mat=[]

    def __init__(self,listeL=None,listeC=None,listeI=None):
        self.L=listeL
        self.C=listeC
        self.I =listeI

    def genererMatrice(self):
        lenl = len(self.L)
        for i in range(lenl-1):
            a = self.L[i]
            b = self.L[i+1]
            v = [0]*(lenl-1)
            while(a < b):
                v[self.I[a]] = self.C[a]
                a += 1
            self.mat.append(v)
        return self.mat

    def genererLCI(self,mate):
        self.L=[0]
        k=0
        self.C=[]
        self.I=[]
        for mat1 in mate:
            for i in range(len(mat1)):
                if mat1[i] != 0 :
                    k+=1
                    self.C.append(mat1[i])
                    self.I.append(i)
            self.L.append(k)
        return (self.L,self.C,self.I)

def main():
    print("generer matrice")
    l = [0, 1, 4, 7, 7]
    c = [1, 2, 3, 4, 5, 6, 7]
    i = [2, 0, 1, 3, 1, 2, 3]
    mat=Matrice(l,c,i)
    m=mat.genererMatrice()
    for i in m:
        print(i)
    print("*****************************************")
    print("generer LCI")
    mat1=Matrice()
    M=[]
    i=[0,0,1,0]
    j=[2,3,0,4]
    k=[0,5,6,7]
    l=[0,0,0,0]
    M.append(i)
    M.append(j)
    M.append(k)
    M.append(l)
    a,b,c=mat1.genererLCI(M)
    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    main()
