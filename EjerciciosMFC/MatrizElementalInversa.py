# -*- coding: utf-8 -*-
""" Por inspección encontrar la matriz inversa de una 
matriz elemental
"""

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np

def PrintMul(a, b):
    print("Matriz a:\n", a) 
    print("Producto ab: \n", np.matmul(a, b))


a = np.array(
    [
        [0, 1],
        [1, 0]
    ]
)


b = np.array(
    [
        [1, 0],
        [5, 1]
    ]
)

binv = np.array(
    [
        [1, 0],
        [-5, 1]
    ]
)

c = np.array(
    [
        [1, 0, 0],
        [0, 1, -3],
        [0, 0, 1]
    ]
)

cinv = np.array(
    [
        [1, 0, 0],
        [0, 1, 3],
        [0, 0, 1]
    ]
)



a = np.array([
    [1, 3],
    [3, 1]
])
ainv = np.array(
    [
        [-1/8, 3/8],
        [3/8, -1/8]
    ]
)

b = np.array([
    [1, -2, 1, 1],
    [2, -3, 3, 0],
    [3, -7, 2, 4],
    [0, 2, 1, 1]
])
binv = np.array([
    [-51, 8, 12, 3],
    [-13, 2, 3, 1],
    [21, -3, -5, -1],
    [5, -1, -1, 0]
])

PrintMul(a, ainv)
PrintMul(b, binv)

l = np.array([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, -1, 1, 0],
        [3, -4/3, 1, 1]
    ])

d = np.array([
        [1, 0, 0, 0],
        [0, -3, 0, 0],
        [0, 0, -2, 0],
        [0, 0, 0, 4]
    ])

u = np.array([
        [1, -1, 1, 2],
        [0, 1, 0, -1],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

print("Resultado:\n")
print(np.matmul(l, np.matmul(d, u)))