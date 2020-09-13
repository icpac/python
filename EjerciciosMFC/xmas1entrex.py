
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 6, 0.01)
#x = [0.1, 6)
#y = [funcion(0.1), funcion(0.1+0.01), funcion(0.1+2*0.01) )

cn2 = np.full(shape=len(x), fill_value=2)

def funcion(t):
    return t + 1 / t

y = funcion(x)

# dibujamos la funcion
plt.plot(x, y, label="x + 1/x", color="green")
# dibujamos la constante 2
plt.plot(x, cn2, label="2", color="blue")
#plt.axhline(y=2, color='k')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.grid("True", which='both')
plt.legend()
plt.show()
