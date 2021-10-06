# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Rango de una matriz """

import numpy as np


def Rango(M):
    print(f"Matriz: \n{M}")
    print(f"Rango de la matriz: {np.linalg.matrix_rank(M)}")

R = np.matrix("1 3 -3 7; 0 3 0 1; 0 0 7 10")
Rango(R)
R = np.matrix("1 2 3 4; -1 3 0 1; -5 6 7 0")
Rango(R)
