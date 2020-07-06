
__autor__= "Tlacaelel Icpac"
__email__= "tlacaelel.icpac@gmail.com"

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve

def grafFuncion(f, domf, ven, pts):
    y = f(domf)
    ax1 = plt.subplot(ven)
    #pinto la identidad
    ax1.plot(domf, domf)
    #pinto la función
    ax1.plot(domf, y)

    if len(pts) > 1:
        ax1.plot(pts, pts, 'o', color='black')

    ax1.grid(True, which='both')
    #eje x
    ax1.axhline(y=0, color='k')
    #eje y
    ax1.axvline(x=0, color='k')

t = symbols('t', real = True)

#definimos dominio de la función    
x = np.arange(-5, 5, 0.1)
f = lambda t: t**2 + 1
pts = solve(t**2 + 1 - t)
grafFuncion(f, x, 121, pts)

"""
x = np.arange(-3, 3, 0.1)
f = lambda t: t**3 - 3*x
pts = solve(t**3 - 3*t - t)
grafFuncion(f, x, 122, pts)"""

x = np.arange(-5, 5, 0.1)
f = lambda t: t**2 - 2
pts = solve(t**2 - 2 - t)
grafFuncion(f, x, 122, pts)

plt.show()
