# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Rango de una matriz """

import numpy as np


def Rango(M):
    print(f"Matriz: \n{M}")
    print(f"Rango de la matriz: {np.linalg.matrix_rank(M)}")

def ImprimeRangos():
    R = np.matrix("1 3 -3 7; 0 3 0 1; 0 0 7 10")
    Rango(R)
    R = np.matrix("1 2 3 4; -1 3 0 1; -5 6 7 0")
    Rango(R)


def ColRen(v, w):
    #A = vwT
    w = w.T
    #w = w.reshape(-1, 1)

    print(f"v: {v} \n {v.shape}")
    print(f"w: {w} \n {w.shape}")
    A = np.matmul(v, w)

    print(f"matriz \n{A}")
    Rango(A) 


ColRen(
np.array([[1], [3]]),
np.array([[-1], [2]])
)

ColRen(
np.array([[4], [0], [2]]),
np.array([[-2], [1]])
)

ColRen(
np.array([[2], [-3]]),
np.array([[1], [3], [-1]])
)

C = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
Rango(C)

"""
1 -2  1
3  2 -3

-3 +6 -3
3  2  -3
0  8  -6

1  -2  1
0  8  -6


1 2 3 
4 5 6 
7 8 9 

1 2 3
3 3 3
6 6 6 

n = 1
n2 = 1 
n2 -1 = 0
a

n=2
4-1 = 3
r2 a   ar 
ar2 ar3


n=3
9-1 = 8
a ar ar2
ar3 ar4 ar5
ar6 ar7 ar8

"""