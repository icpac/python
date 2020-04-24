"""

Tlacaelel Icpac
tlacaelel.icpac@gmail.com

Graficamos dos funciones para comparar su
comportamiento cerca del punto x = 2
Además imprimimos el limite cuando x se acerca a 2
que no existe o decimos que es infinito

"""
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# Intervalo
x = np.arange(0, 3, .1)

# Dibuja las funciones 
plt.plot(x, x**2 -x + 6, label="x^2 - x + 6")
plt.plot(x, x-2, label="x-2")

plt.legend()

plt.title("Comparar comportamiento:")
plt.grid(True)

#Ejes
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('x')
plt.ylabel('y')

#Imprimimos el limite cuando x se acerca a 2
x=Symbol("x")
print ("El límite, cuando x se acerca a 2: ",
       limit ((x**2 -x + 6) / (x-2), x, 2))


plt.show()
