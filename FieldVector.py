
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x1,y1 = np.meshgrid(np.linspace(-3.5, 1.5, 10),np.linspace(0,0,1))
x2,y2 = np.meshgrid(np.linspace(-2.5, 2.5, 10),np.linspace(0,0,1))
x3,y3 = np.meshgrid(np.linspace(-1.5, 3.5, 10),np.linspace(0,0,1))

z1 = np.arange(-5, 2.5, .01)
z2 = np.arange(-2.5, 2.5, .01)
z3 = np.arange(-2.5, 5, .01)

funcion1 = lambda t: -3*t - t**2
funcion2 = lambda t: - t**2
funcion3 = lambda t: 3*t - t**2

t1 = funcion1(z1)
t2 = funcion2(z2)
t3 = funcion3(z3)

ax1 = plt.subplot(221)
ax1.plot(z1, t1, label="y = -3x - x**2", color="green")
#eje x
ax1.axhline(y=0, color='k')
#eje y
ax1.axvline(x=0, color='k')
# Cuadrante
ax1.grid(True, which='both')
ax1.legend()

u1 = -3*x1 - x1**2
v1 = 0

ax1.quiver(x1,y1,u1,v1)

ax1.plot([0], [0], marker='o', markersize=8, color="black", fillstyle=Line2D.fillStyles[0])
ax1.plot([-3], [0], marker='o', markersize=8, color="black", fillstyle=Line2D.fillStyles[5])


ax2 = plt.subplot(222)
ax2.plot(z2, t2, label="y = -x**2", color="blue")
#eje x
ax2.axhline(y=0, color='k')
#eje y
ax2.axvline(x=0, color='k')
# Cuadrante
ax2.grid(True, which='both')
ax2.legend()

u2 = -x2**2
v2 = 0

ax2.quiver(x2,y2,u2,v2)

ax2.plot([0], [0], marker='o', markersize=8, color="black", fillstyle=Line2D.fillStyles[2])



ax3 = plt.subplot(223)
ax3.plot(z3, t3, label="y = 3x -x**2", color="red")
#eje x
ax3.axhline(y=0, color='k')
#eje y
ax3.axvline(x=0, color='k')
# Cuadrante
ax3.grid(True, which='both')
ax3.legend()

u3 = 3*x3 -x3**2
v3 = 0

ax3.quiver(x3,y3,u3,v3)

ax3.plot([0], [0], marker='o', markersize=8, color="black", fillstyle=Line2D.fillStyles[5])
ax3.plot([3], [0], marker='o', markersize=8, color="black", fillstyle=Line2D.fillStyles[0])


plt.show()
