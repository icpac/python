
import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

P = np.array([
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
])

"""
print("A:\n", A)
print("P^{T}:\n", np.transpose(P))
print("Producto AP^{T}: \n", np.matmul(A, np.transpose(P)))

print("Producto: PAP^{T}\n", np.matmul(P, np.matmul(A, np.transpose(P))))"""


def Ej1_6_16():
    v = np.array([
        [1],
        [3]
    ])
    w = np.array([
        [-1],
        [2]
    ])

    r = np.matmul(v, np.transpose(w))
    print(f"Producto: vw^T \n {v}, \n{np.transpose(w)} = \n", r)

    I = np.identity(2, np.int16)
    print("Identidad:\n", I)

    A = I - r
    print("Matriz A:\n", A) 

    print("Inversa A: \n", np.linalg.inv(A)) 

    c = .25
    i = c*np.matmul(v, np.transpose(w))
    print(f"Producto: cvw^T \n {c}, \n{v}, \n{np.transpose(w)} = \n", r)

    A = I - i
    print("Matriz A:\n", A) 




Ej1_6_16()
