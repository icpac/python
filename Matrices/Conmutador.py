# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Conmutador """

import numpy as np
import sympy as sp

def Conmutador(P, Q):
    return P*Q - Q*P

P = np.array([
[-1,3],
[3,-1],
])

Q = np.array([
[1,7],
[7,1],
])

print(f"Conmutador de \n{P}, \n{Q}: \n{Conmutador(P, Q)}")

P = np.array([
[0, -1, 0],
[1,0,0],
[0,0,1]
])

Q = np.array([
[1,0,0],
[0,0, -1],
[0,1, 0],
])

print(f"Conmutador de \n{P}, \n{Q}: \n{Conmutador(P, Q)}")


a11,a12,a13,a21,a22,a23,a31,a32,a33 = sp.symbols('a11,a12,a13,a21,a22,a23,a31,a32,a33')
b11,b12,b13,b21,b22,b23,b31,b32,b33 = sp.symbols('b11,b12,b13,b21,b22,b23,b31,b32,b33')

A = sp.Matrix([
[a11,a12,a13],
[a21,a22,a23], 
[a31,a32,a33]])

B = sp.Matrix([
[b11,b12,b13],
[b21,b22,b23], 
[b31,b32,b33]])

print (A*B-B*A)
traceM=sp.Trace(A*B-B*A)

print(traceM)
print(sp.Trace(A*B-B*A))
conm = A*B-B*A

print(f"\n {conm.trace()}")
print(f"\n {conm.diagonal()}")