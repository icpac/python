import numpy as np

L = np.array([
    [1, 0, 0, 0],
    [-1, 1, 0, 0],
    [0, 2, 1, 0],
    [3, 3, 6/5, 1],
])

D = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -5, 0],
    [0, 0, 0, -49/5],
])

LT = np.array([
    [1, -1, 0, 3],
    [0, 1, 2, 3],
    [0, 0, 1, 6/5],
    [0, 0, 0, 1],
])


print("La matriz A: \n", np.round(np.matmul(np.matmul(L, D), LT)))
