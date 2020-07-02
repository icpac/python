
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
from sympy import *

# Primera solución
print("Obtener la órbita de x^2, en 1/2")
print("primera solución")
print(.5**2)
print((.5**2)**2)
print(((.5**2)**2)**2)
print((((.5**2)**2)**2)**2)
print(((((.5**2)**2)**2)**2)**2)


#segunda solucion
print("\nsegunda solución")
x0 = 1/2
print(x0)
for i in range(5):
    x0 = x0**2
    print(x0)

    
#tercera solución
print("\ntercera solución")
x1 = np.arange(0.5, 0.6, 0.1)
print(Rational(x1[0]))
f = lambda t: t**2

for i in range(5):
    print(Rational(f(x1)[0]))
    x1 =  f(x1)    


#cuarta solucion
def evaluacion(f, x0, tnts):
    print(Rational(x0[0]))
    for i in range(tnts):
        print(Rational(f(x0)[0]))
        x0 = f(x0)    


print("\nCuarta solucion")
x1 = np.arange(0.5, 0.6, 0.1)
evaluacion(f, x1, 5)

print("\nLa otra función")
x1 = np.arange(0, 0.1, 0.1)
g = lambda t: t**2 + 1
evaluacion(g, x1, 10)
