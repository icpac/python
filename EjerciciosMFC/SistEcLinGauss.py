# -*- coding: utf-8 -*-

""" Eliminación Gaussiana, matrices regulares """ 

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np


def Gauss(A):
    n = A.shape[0]

    for j in range(0, n):
        if A[j][j] == 0: 
            print("La matriz no es Regular ")
            return None
        else:
            for i in range(j+1, n):
                lij = A[i,j]/A[j,j]
                A[i] = A[i] - lij * A[j]

    return A


def suma(A, x, i):
    sum = 0
    n = A.shape[0]
    for j in range(n-1, i, -1):
        sum += A[i][j]*x[j]
    return sum


def Sustitucion(A):
    n = A.shape[0]
    x = np.zeros(n)
    x[n-1] = A[n-1,n]/ A[n-1, n-1]
    
    for i in range ((n-1)-1, 0-1, -1):
        x[i] = 1/ A[i][i] * (A[i, n] - suma(A, x, i)) 
    return x




M = np.array(
    [
        [1, 2, 1, 2],
        [2, 6, 1, 7],
        [1, 1, 4, 3]
    ], dtype='f'
)

A = M.copy()

print("Matriz aumentada: \n", M)
Gaus = Gauss(M)
if Gaus.all() != None:
    print("Matriz Triangular Superior: \n", np.round(Gaus, 3))
    Sol = Sustitucion(Gaus).reshape(3, 1)
    print("Solucion:\n", np.round(Sol, 3))

    A = np.delete(A, -1, axis=1)
    #Sol = np.array(Sol).reshape(3, 1)
    #print("Solucion: \n", Sol)
    print("Matriz de Coeficientes :\n", A)
    print("Comprueba la solucion: \n", np.round(np.matmul(A, Sol), 2)) 