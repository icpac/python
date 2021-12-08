import numpy as np
from GaussNoS import GaussNoS


def Solucion(A, x):
    b = np.matmul(A, x)
    print (f"B: {b}\n")

    res = GaussNoS(A)
    if res != None:
        print(f"Forma Escalonada: {A}\n")
    else:
        print(f"Es singular: \n{A}\n") 

def AlgunasS(A, x, c):
    slcero = np.array([[1],
    [1],
    [1]])
    sg = x + c*slcero

    print(f"Resultado:  \n{np.matmul(A, sg)}") 

if __name__ == "__main__":
    x = np.array(
    [[1],
    [2],
    [3]])

    A = np.array([
    [ 1, -1,  0],
    [-1,  0,  1],
    [ 0,  1, -1]
    ])
    M = A.copy()
    Solucion(A, x)
    for i in range(0, 6):
        AlgunasS(M, x, i*.5)