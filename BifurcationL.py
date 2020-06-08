
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 1, .01)
x1 = np.arange(1, 3, .01)
x2 = np.arange(-4, 0, .01)
x3 = np.arange(0, 3, .01)

funcion = lambda t: .5*(t-1)
funcion2 = lambda t: 0*t

y = funcion2(x)
y1 = funcion(x1)
y2 = funcion2(x2)
y3 = funcion2(x3)

ax1 = plt.subplot(111)
ax1.margins(.09)
ax1.plot(x, y, linewidth=3.0, color="black")
ax1.plot(x1, y1, color="black")
ax1.plot(x3, y3, 'r--', color="black")

#eje y
ax1.axvline(x=0, color='b')

ax1.text(-.1, 1, r'$n$')
ax1.text(-.1, 0, r'$0$')
ax1.text(.4, .05, r'$lámpara$')
ax1.text(.96, -.05, r'$k / G$')
ax1.text(2.96, -.05, r'$N_0$')
ax1.text(3, 1, r'$láser$')

plt.show()
