__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np

def Resuelve(M, C):
    """ Aunque parece que linalg está obsolete 
    La matriz debe ser cuadrada !
    """
    x = np.linalg.solve(M, C)
    print(f"Matriz de coeficientes \n{M}")
    print(f"Términos constantes \n {C}") 
    print(f"La solución es: \n {x}")



a = np.array([
    [1, 1, 3, -2, -1], 
    [5, -2, 3, 7, 8],
    [-3, -1, 2, 7, 5],
    [5, 3, 1, -2, -7]])

b = np.array([1, 3, 2, 3])

Resuelve(a, b)