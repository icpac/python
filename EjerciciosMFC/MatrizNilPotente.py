# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Vemos si una matriz es Nilpotente """

import numpy as np

def Nilpotente(M):
    intentos = 0
    _M = M.copy()
    Ceros = np.zeros(M.shape, M.dtype)
    while intentos < 10 and not np.array_equal(_M, Ceros):
        _M = np.matmul(M, _M)
        intentos += 1
    return intentos


N = np.array(
    [
        [0, 1, 2],
        [0, 0, 1],
        [0, 0, 0]
    ]
)

N = np.array(
    [
        [1, 1, 1, 1], 
        [1, 1, 1, 1], 
        [-1, -1, -1, -2],
        [-1, -1, -1, -1]
    ]
)

k = Nilpotente(N)
if k < 10:
    print("La matriz fue Nilpotente: \n", N, "\n", k+1)
else:
    print("Con k intentos no fue: ", k+1)