# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"


""" Dibuja una función y tres puntos en ella """

import numpy as np
import matplotlib.pyplot as plt

#dominio 
x = np.arange(0.1, 6, 0.01)
x = np.arange(-3, 3, 0.1)

def funcion(t):
    #return -t**2 + t + 6
    #return np.sin(3*t)
    #return np.cos(3*x-np.pi/2)
    #return np.cos(t)*np.sin(t)
    return 1/2 * np.cos(2*t-np.pi/2)

y = funcion(x)

ptsx = [1, 2, 3]
ptsy = [6, 4, 0]

tit = "-x**2+x+6"
tit = "sen 3x"
tit = "cos(3*x-pi/2)"
tit = "1/2 * cos(2*t-pi/2)"
# dibujamos la funcion
plt.plot(x, y, label=tit, color="green")

if tit == "-x**2+x+6":
    #punto en ella 
    plt.plot(ptsx, ptsy, 'o', color="red")
    plt.annotate("(1, 6)", (1, 6))
    plt.annotate("(2, 4)", (2, 4))
    plt.annotate("(3, 0)", (3, 0))

#ejes 
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.grid("True", which='both')
plt.legend()
plt.show()




