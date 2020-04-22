"""
Carlos Javier López Cruz
javier1604@gmail.com
Se dibujan dos funciones para ver su comportamiento cerca del 1
y = 10 (x - 1)
y = x - 1
"""
import numpy as np
import matplotlib.pyplot as plt


# intervalo en x, dominio de las funciones
x = np.arange(0, 4, .01)
funcion = lambda t: 10*(t - 1)
funcion2 = lambda t: t - 1
y = funcion(x)
y1 = funcion2(x)



plt.plot(x, y, label="y = 10(x-1)", color="green")
plt.plot(x, y1, label="y = x - 1", color="blue")
#eje x
plt.axhline(y=0, color='k')
#eje y
plt.axvline(x=0, color='k')

# Cuadrante
plt.grid(True, which='both')
plt.legend()
# Muestra la imagen
plt.show()
