# -*- coding: utf-8 -*-

""" Eliminación Gaussiana, matrices regulares,
no singulares """ 

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np


def Ceros(R, k, j, n):
    return False

def GausNonS(A):
    n = A.shape[0]
    print(np.argwhere(A == 0))
    for j in range (0, n):
        #zz = np.argwhere(A[j] == 0)
        res = np.where(A[j] == 0)[0]
        if Ceros(A[j], j, j, n):
            print("A es singular")
        if A[j,j] == 0:
            #falta algo aquí
            None

def Gauss(A, Mo):
    n = A.shape[0]

    for j in range(0, n):
        if A[j][j] == 0: 
            print("La matriz no es Regular ")
            return None

        """
        max_index = abs(A).argmax(axis=0)
        M = max_index[j]
        if M > j:
            A[[M, j]] = A[[j, M]]
            Mo[[M, j]] = Mo[[j, M]]"""



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
    x = np.zeros(n, dtype=A.dtype)
    x[n-1] = A[n-1,n]/ A[n-1, n-1]
    
    for i in range ((n-1)-1, 0-1, -1):
        x[i] = 1/ A[i][i] * (A[i, n] - suma(A, x, i)) 
    return x



M = np.array(
    [
        [1-1j, 2+0j, 0+1j],
        [0-1j, 1+1j, -1+0j]
    ], dtype=np.complex_
) 

M = np.array(
    [
        [1+1j, 0+1j, 2+2j, 0+0j],
        [1-1j, 2+0j, 0+1j, 0+0j],
        [3-3j, 0+1j, 3-11j, 6+0j]
    ], dtype=np.complex_
)

M = np.array(
    [
        [1, 2, 1, 2],
        [2, 6, 1, 7],
        [1, 1, 4, 3]
    ], dtype='f'
)

M = np.array(
    [
        [1, 1, 1, 6],
        [4, 2, 1, 4],
        [9, 3, 1, 0]
    ], dtype= 'f'
)


M = np.array([
        [.1, 2.7, 10],
        [1.0, 0.5, -6.0]
    ], dtype= 'f')

M = np.array([
        [1.0, 0.5, -6.0],
        [.1, 2.7, 10]
    ], dtype= 'f')


M = np.array([
        [1., -5., -1., 1.],
        [1/6, -5/6, 1., 0.],
        [2., -1., 0., 3.]
    ], dtype= 'f')


"""
M = np.array([
        [97, 25, -35, 39],
        [-22, 35, 33, -15],
        [4, 1, -3, -3]
    ], dtype= 'f')"""

def SolcNon(M):
    A = M.copy
    GausNonS(M)

def Otra(M):
    A = M.copy()

    print("Matriz aumentada: \n", M)
    Gaus = Gauss(M, A)
    if Gaus.all() != None:
        #print("Matriz Triangular Superior: \n", np.round(Gaus, 3))
        print("Matriz Triangular Superior: \n", Gaus)
        n = M.shape[0]
        Sol = Sustitucion(Gaus).reshape(n, 1)
        #print("Solucion:\n", np.round(Sol, 3))
        print("Solucion:\n", Sol)

        print("Matriz Intercambiada :\n", A)
        A = np.delete(A, -1, axis=1)
        print("Matriz de Coeficientes :\n", A)
        print("Comprueba la solucion: \n", np.round(np.matmul(A, Sol), 2)) 
        #print("Comprueba la solucion: \n", np.matmul(A, Sol)) 
        print("\n\n")

#SolcNon(M)
M = np.array([
        [.1, 2.7, 10],
        [1.0, 0.5, -6.0]
    ], dtype= 'f')

M1 = np.array([
        [1., -5., -1., 1.],
        [1/6, -5/6, 1., 0.],
        [2., -1., 0., 3.]
    ], dtype= 'f')

M2 = np.array([
        [1, 4, -3, -3], 
        [25, 97, -35, 39],
        [35, -22, 33, -15]
    ], dtype= 'f')

M3 = np.array([
        [0.2, 2, -3, 6], 
        [5, 43, 27, 58],
        [3, 23, -42, -87]
    ], dtype= 'f')

#Otra(M)
#Otra(M2)
#Otra(M3)
Otra(M1)
