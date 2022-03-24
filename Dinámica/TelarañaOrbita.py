"""
Tlacaelel Icpac
tlacaelel.icpac@gmail.com

Iteración de una funcion:
telaraña con una
recta= 2x
parábola= x^2 - 2
parábola2 = 4*x*(1-x): [-.1, 1.2] x0 = .05

El usuario captura el intervalo a considerar
y el punto inicial
"""

import numpy as np
import matplotlib.pyplot as plt

xdi = float(input("Extremo inicial: "))
xdf = float(input("Extremo final: "))

print (f"la función va estar definida desde: {xdi} hasta: {xdf}")
paso = 0.01

x = np.arange(xdi, xdf, paso)
funcion = lambda t: 4*t*(1-t)
#funcion = lambda t: t**2 - 2
#funcion = lambda t: 2*t
y = funcion(x)

plt.plot(x, x, color="blue", label="y = x")
plt.plot(x, y, color="green", label="y = 4x(1-x)")

x0 = float(input("Valor inicial: "))
itera = 1
limiteItera = 25

plt.plot([x0, x0], [x0, funcion(x0)], color = 'pink')
while funcion(x0) > xdi and funcion(x0) < xdf and itera < limiteItera:
    plt.plot([x0, funcion(x0)], [funcion(x0), funcion(x0)], color = 'r')
    x0 = funcion(x0)
    plt.plot([x0, x0], [x0, funcion(x0)], color = 'pink')
    itera += 1


#Ejes
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.grid(True)
plt.legend()
plt.show()
