# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Expresiones algebraicas con sympy """


from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

print(expand((1+2**.5)**3))
print(7+5*2**.5)

a, b, c= symbols('a b c')
print("Expande la expresion: (a-b-c)(a+b+c)") 
print(expand((a-b-c)*(a+b+c)))
print("Expande la expresion: (a-b+c)(a+b-c)") 
print(expand((a-b+c)*(a+b-c)))

print(" ".join(str(4**i) for i in range(1, 15)))
print("")
print(5**2+12**2, 13**2) 