# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"



""" Operaciones con binarios """

""" Suma """
b1 = 11100
b2 =  1110

resultado = int(str(b1), 2)+int(str(b2), 2)
print(f"es un entero:  {bin(resultado)[2:]}")

""" Producto """
 #101010
b1 = 1110
b2 =  11

resultado = int(str(b1), 2) * int(str(b2), 2)
print(f"es un entero:  {bin(resultado)[2:]}")

