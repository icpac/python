# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Conmutador """

import numpy as np

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
