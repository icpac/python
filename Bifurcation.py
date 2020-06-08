
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 3, .01)
x1 = np.arange(-3, 0, .01)
x2 = np.arange(-4, 0, .01)
x3 = np.arange(0, 4, .01)

funcion = lambda t: t
funcion2 = lambda t: 0*t

y = funcion(x)
y1 = funcion(x1)
y2 = funcion2(x2)
y3 = funcion2(x3)

plt.plot(x, y, color="black")
plt.plot(x1, y1, 'r--', color="black")
plt.plot(x2, y2, linewidth=3.0, color="black")
plt.plot(x3, y3, 'r--', color="black")

#eje y
plt.axvline(x=0, color='b')

plt.text(4, 0, r'$inestable$')
plt.text(3, 3, r'$estable$')
plt.text(-.5, 3, r'$x$')
plt.text(-4, .1, r'$estable$')
plt.text(-2.8, -3, r'$inestable$')
plt.text(3.5, -.2, r'$r$')

plt.show()
