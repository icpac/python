import numpy as np

L = np.array([
    [1, 0, 0, 0, 0],
    [2, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [4, 1, 0, 1, 0 ],
    [0, 1, 0, 0, 1]
])

U = np.array([
    [1, -1, 2, 1],
    [0, 3, -5, -2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])

print(np.matmul(L, U))


P = np.array([
[0, 1, 0 ],
[0, 0, 1 ],
[1, 0, 0 ]
])

A = np.array([
[0, 0,  0, 3,  1],
[1, 2, -3, 1, -2],
[2, 4, -2, 1, -2] 
])

L = np.array([
[1, 0, 0 ],
[2, 1, 0 ],
[0, 0, 1 ]
])

U = np.array([
  [1, 2, -3,  1, -2],
  [0, 0,  4, -1,  2],
  [0, 0,  0,  3,  1]
])

print(np.matmul(P, A))
print(np.matmul(L, U))
#http://132.248.17.160/escuela/style/img/Redes.pdf