#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

print(expand((1+2**.5)**3))
print(7+5*2**.5)

print(" ".join(str(4**i) for i in range(1, 15)))
print("")
print(5**2+12**2, 13**2) 