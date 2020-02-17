#!/usr/bin/env python

# class Matrice:
#     mat=[]
#
#     def __init__(self,listeL,listeC,listeI):
#         self.l=listeL
#         self.c=listeC
#         self.i = listeI
#
#      def genererMatrice(self):
#          l=0
#          c=0
#          i=0
#          w=0
#          for a in range(len(self.c)):
#              mat1=[]
#              for k in range(len(self.c)):
#                  if w == self.l[w+1]:
#                     mat1[k] =0
#                 elif w < self.l[w+1]:
#                     if k= self.i[i]:
#                         mat1[k]=self.c[c]
#                         c+=1
#                     else :
#                         mat1[k]=0
#                 i+=1
#             self.mat.append(mat1)

def genererLCI(mat):
    L=[0]
    k=0
    C=[]
    I=[]
    for mat1 in mat:
        for i in range(len(mat1)):
            if mat1[i] != 0 :
                k+=1
                C.append(mat1[i])
                I.append(i)
        L.append(k)
    return (L,C,I)

def testerMatrice():
    M=[]
    i=[0,3,5,8]
    j=[1,0,2,0]
    k=[0,0,0,0]
    l=[0,3,0,0]
    M.append(i)
    M.append(j)
    M.append(k)
    M.append(l)
    #print(M)
    a,b,c = genererLCI(M)
    print("L  ",a)
    print("C  ",b)
    print("I  ",c)

def testerMatrice2():
    M=[]
    i=[0,0,1,0]
    j=[2,3,0,4]
    k=[0,5,6,7]
    l=[0,0,0,0]
    M.append(i)
    M.append(j)
    M.append(k)
    M.append(l)
    #print(M)
    a,b,c = genererLCI(M)
    print("L  ",a)
    print("C  ",b)
    print("I  ",c)
    genererMatrice(a,b,c)

def genererMatrice(listeL,listeC,listeI):
    mat=[]
    l=0
    c=0
    i=0
    w=0
    for a in range(len(listeC)):
        mat1=[]
        for b in range(len(listeC)):
            if w == listeL[w+1]:
                mat1[b]=0
            elif w< listeL[w+1]:
                if b == listeI[i]:
                    mat1[b]=listeC[c]
                    c+=1
                else:
                    mat1[b]=0
            i+=1
        w+=1
        mat.append(mat1)
    print(mat)
    
def lci_to_matrice(L, C, I):
    matrice = []
    lenl = len(L)
    for i in range(lenl-1):
        a = l[i]
        b = l[i+1]
        v = [0]*(lenl-1)
        while(a < b):
            v[I[a]] = C[a]
            a += 1
        matrice.append(v)
    return matrice
#print(matriceTitle("outfevrier.xml"))
print("Matrice 1  ",testerMatrice())
print("Matrice 2  ",testerMatrice2())
