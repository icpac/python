import numpy as np

def di(i, L, U, A):
    U[i+1][i+1] = A[i+1][i+1] - L[i+1][i] * U[i][i+1]

def li(i, L, U, A):
    L[i+1][i] = A[i+1][i]/U[i][i]

def ur(i, U, A):
    U[i][i+1] = A[i][i+1]

def dq(i, U, A):
    U[i][i] = A[i][i]

def LU (A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=A.dtype)
    U = np.zeros_like(A, dtype=A.dtype)

    np.fill_diagonal(L, 1)
    dq(1-1, U, A)
    for d in range(n-1):
        ur(d, U, A)
        li(d, L, U, A)
        di(d, L, U, A)
    di(d, L, U, A)

    return L, U

def ci(i, c, b, L):
    c[i+1] = b[i+1]-L[i+1][i]*c[i]

def xi(i, c, x, U):
    if i+1 == x.shape[0]:
        xi1 = 0
    else:
        xi1 = U[i][i+1]*x[i+1]
    x[i] = (c[i] - xi1) / U[i][i]


def Solucion(A, L, U, b):
    n = A.shape[0]

    c = np.zeros_like(b, dtype=b.dtype)
    x = np.zeros_like(b, dtype=b.dtype)
    c[0] = b[0]
    for i in range(n-1):
        ci(i, c, b, L)

    xi(n-1, c, x, U)
    for i in range((n-1)-1, 0-1, -1):
        xi(i, c, x, U) 

    return x


def Imprime(A, b):
    ret = LU(A)
    x = Solucion(A, ret[0], ret[1], b)

    print(np.matmul(ret[0], ret[1]), f"\n A: \n{A}") 
    print(np.matmul(A, x.reshape(-1, 1)))
    print(f"La solución fue: \n{x}")


if __name__ == "__main__":
    A = np.array([
    [1, 2, 0],
    [-1, -1, 1],
    [0, -2, 3]
    ], dtype= 'f')
    b = np.array([4, -1, 6], dtype='f')

    A = np.array([
    [1, -1, 0, 0],
    [-1, 2, 1, 0],
    [0, -1, 4, 1],
    [0, 0, -5, 6]
    ], dtype='f')
    b = np.array([1, 0, 6, 7], dtype='f')

    A = np.array([
    [1, 2, 0, 0],
    [-1, -3, 0, 0],
    [0, -1, 4, -1],
    [0, 0, -1, -1]
    ], dtype='f')
    b = np.array([0, -2, -3, 1], dtype='f')
    Imprime(A, b)
    