"""
Carlos Javier López Cruz
javier1604@gmail.com
Iteración de una funcion: telaraña con una recta= 2x
"""

import numpy as np
import matplotlib.pyplot as plt

xdi = 3
paso = 0.01

x = np.arange(-xdi, xdi+.1, paso)
funcion = lambda t: 2*t
y = funcion(x)

plt.plot(x, x, color="blue", label="y = x")
plt.plot(x, y, color="green", label="y = 2x")

x0 = .01
itera = 1
limiteItera = 25

plt.plot([x0, x0], [x0, funcion(x0)], color = 'pink')
while abs(funcion(x0)) < xdi and abs(funcion(x0)) > .00001 and itera < limiteItera:
    plt.plot([x0, funcion(x0)], [funcion(x0), funcion(x0)], color = 'r')
    x0 = funcion(x0)
    plt.plot([x0, x0], [x0, funcion(x0)], color = 'pink')
    itera += 1


plt.grid(True)
plt.legend()
plt.show()
