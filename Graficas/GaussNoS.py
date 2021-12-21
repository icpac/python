
import numpy as np


def GaussNoS(A):
    n = A.shape[0]
    inter = 0
    for j in range(0, n):
        col = A[j:, j]
        if np.all(col == 0):
            print('A es singular')
            return None
        if col[0] == 0:
            M = abs(col).argmax()
            if M > 0:
                A[[M+j, j]] = A[[j, M+j]]    
                inter += 1

        for i in range(j+1, n):
            lij = A[i, j]/ A[j, j]
            A[i] = A[i] - lij*A[j]
    return A, inter


if __name__ == "__main__":
    A = np.array([
[1, -2,  1,  4, -5],
[1,  1, -2,  3, -3], 
[2, -1, -1,  2,  2],
[5, -1,  0,  5,  5],
[2,  2,  0,  4, -1]
], dtype='f')
    A = np.array([
        [-1, 0, -3],
        [2, 1, 1],
        [-3, 2, 0]
    ])
    res = GaussNoS(A)
    Mt = res[0]
    inter = res[1]
    print(f"{Mt}\n")
    diag = np.diag(Mt)
    prodDia = np.prod(diag)
    print(f"{diag}\n")
    print(f"El producto de la diagonal {prodDia}")
    print(f"El determinante es {(-1)**inter*prodDia}")