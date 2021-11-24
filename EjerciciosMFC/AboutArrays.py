
import numpy as np

def Swap():
    a = np.array([[4,3, 1],[5 ,7, 0],[9, 9, 3],[8, 2, 4]]) 
    print(a)

    a[[0, 2]] = a[[2, 0]]
    print(a)


def MaxColumn():
    A = np.asarray(
    [[1, 2, 3, 4, 5],
     [2, 4, 5, 8, 7],
     [-9, 8, 4, 5, 2],
     [1, 2, 4, 7, 2],
     [5, 9, 8, 7, 6],
     [1, 2, 5, 4, 3]])
    print(A)

    max = A.max(axis=0, keepdims=True)
    max_index = abs(A).argmax(axis=0)
    min_index = A.argmin(axis=0)

    print('Max:', max)
    print('Max Index:', max_index)
    print("Min Index:", min_index)


MaxColumn()