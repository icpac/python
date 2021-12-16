__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"


import numpy as np

def Traza(A, B):
    """ Multiplicación y traza """
    AB = np.matmul(A, B)
    print(np.matrix.trace(AB))


if __name__ == "__main__":
    """ La matriz de prueba """
    A = np.array(
    [
        [1, 2, -1],
        [2, 1, 3],
    ])

    B = np.array(
    [
        [5, 4],
        [6, 5],
        [1, 0]
    ])

    Traza(A, B)
    Traza(B, A)

    B = np.array(
    [
        [2, 0],
        [0, 2],
    ])

    Traza(B, B)

