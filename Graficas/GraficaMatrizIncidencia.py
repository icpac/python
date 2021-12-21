import numpy as np
from MatrizIncidencia import *

from GaussNoS import GaussNoS

A = np.array([
    [-1, 1,0, 0],
    [ 0,-1,1, 0],
    [ 0, 0,1,-1],
    [ 0, 1,0,-1],
    [-1, 0,1, 0]
])


Etq = Etiquetas(A)
MuestraDiGrafica(A, Etq, PosRegular(A.shape[1]))

res = GaussNoS(A)
if res != None:
    print(f"Forma Escalonada: {A}\n")
else:
    print(f"Es singular: \n{A}\n") 

At = A.T
res = GaussNoS(At)
if res != None:
    print(f"Forma Escalonada: {At}\n")
else:
    print(f"Es singular: \n{At}\n") 

"""
Rango = 3
Dimensiones
dim img A = dim coimg A = 3
dim ker A = n - r  = 4 - 3 = 1
dim coker A = m - r = 5 - 3 = 2

Base para el kernel, y el cokernel
x4
x3 = x4
x2 = x3 = x4
x1 = x2 = x3 = x4

x4 (1 1 1 1), una base para el kerA

x5
x4
x3 = 0
x2 = 0
x1 = 0

x4(0 0 0 1 0)  x5(0 0 0 0 1)



A = At  es simetrica de nxn
Entonces
(Av).w = v.(Aw)  v, w en Rn


"""

