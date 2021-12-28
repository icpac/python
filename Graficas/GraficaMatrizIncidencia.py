import numpy as np

from MatrizIncidencia import *
from GaussNoS import GaussNoS

A = np.array([
    [-1,  1, 0,  0 ],
    [ 0, -1, 1,  0],
    [ 0,  0, 1, -1],
    [ 0,  1, 0, -1],
    [-1,  0, 1,  0]
])

cA = A.copy()
At = A.T.copy()
cAt = At.copy()

et = Etiquetas(A)
#MuestraDiGrafica(A, et, PosRegular(A.shape[1]))

res = GaussNoS(At)
if res != None:
    print(f"forma escalonada: \n{At}")
else:
    print(f"Es singular: \n {At}")


b1 = np.array([1, 1, 1, 1])
m = -55
print("Kernel")
print(np.matmul(A, m*b1))

b1 = np.array([ 0,  1, -1, 1, 0])
b2 = np.array([-1, -1,  0, 0, 1])
m = 105
n = -33
print("CoKernel")
print(np.matmul(At, m*b1 + n*b2)) 
