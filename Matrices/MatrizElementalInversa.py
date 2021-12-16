# -*- coding: utf-8 -*-
""" Por inspección encontrar la matriz inversa de una 
matriz elemental
"""

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
from fractions import Fraction
import sympy as sy

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
#PrintMul(c, cinv)


D1 = np.array(
    [
        [1, 2, 0],
        [2, 1, 0], 
        [0,0, 3]
    ]
)

D1i = np.array(
    [
        [-1/3, 2/3, 0],
        [2/3, -1/3, 0], 
        [0,0, 1/3]
    ]
)





D2 = np.array(
    [
        [1, -1, 0, 0],
        [2, -1, 0, 0], 
        [0, 0, 1, 3],
        [0, 0, 2, 5]
    ]
)

D2i = np.array(
    [
        [-1, 1, 0, 0],
        [-2, 1, 0, 0], 
        [0, 0, -5, 3],
        [0, 0, 2, -1]
    ]
)


b = np.array(
    [
        [1, 3],
        [3, 1]
    ]
)

binv = np.array(
    [
        [-1/8, 3/8],
        [3/8, -1/8]
    ]
)

b2 = np.array(
    [
        [1, -2, 1, 1],
        [2, -3, 3, 0], 
        [3, -7, 2, 4],
        [0, 2, 1, 1]
    ]
)

b2i = np.array(
    [
        [-51, 8, 12, 3],
        [-13, 2, 3, 1], 
        [21, -3, -5, -1],
        [5, -1, -1, 0]
    ]
)

#PrintMul(b, binv)
#PrintMul(b2, b2i)

E1 = np.array(
    [
        [Fraction(2/3**(1/2)), 0],
        #[sy.Rational(2/3**(1/2)), 0]
        [0, 1]
    ]
)

E1 = E1 + Fraction()
#print(f"E1: {E1}")

E_1 = np.array(
    [
        [3**(1/2) /2, 0],
        [0, 1]
    ]
)
E2 = np.array(
    [
        [1, 0],
        [-1/2, 1]
    ]
)
E_2 = np.array(
    [
        [1, 0],
        [1/2, 1]
    ]
)
E3 = np.array(
    [
        [1, 0],
        [0, 3**(1/2)/2]
    ]
)
E_3 = np.array(
    [
        [1, 0],
        [0, 2/3**(1/2)]
    ]
)
E4 = np.array(
    [
        [1, 1/3**(1/2)],
        [0, 1]
    ]
)
E_4 = np.array(
    [
        [1, -1/ 3**(1/2)],
        [0, 1]
    ]
)

#print(np.matmul(E_1, E1))
#print(np.matmul(E_2, E2))
#print(np.matmul(E_3, E3))
#print(np.matmul(E_4, E4))

#import fractions
#np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
#A = np.matmul(np.matmul(E_1, E_2), np.matmul(E_3, E_4))
#print(A)

#print(Fraction(3**(1/2)/2))


c1 = np.array([
    [1+0j, 0+0j, 0+1j],
    [0+1j, -1+0j, 1+1j],
    [0-3j, 1-1j, 1+1j]
])

c1_i = np.array([
    [3+1j, -1-1j, 0-1j],
    [-4+4j, 2-1j, 2+1j],
    [-1+2j, 1-1j, 1+0j]
])

print("Y el producto es:")
print(np.matmul(c1, c1_i))
print(np.matmul(c1_i, c1))



d1 = np.array([
    [1, 1, 0, 0],
    [2, 3, 0, -1],
    [0, -1, -1, 1],
    [0, 0, 1, -1]
])

d1_i = np.array([
    [1, 0, 1, 1],
    [0, 0, -1, -1],
    [2, -1, -1, 0],
    [2, -1, -1, -1]
])

#print("Y el producto es:")
#print(np.matmul(d1, d1_i))
#print(np.matmul(d1_i, d1))



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