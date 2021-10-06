# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Permutaciones """ 

import itertools


def prinPermuta(num):
    print("Permutaciones")
    for p in itertools.permutations(range(1, num)):
        print(p)

def esPar(permuta):
    inver = 0
    for i, num in enumerate(permuta, start=1):
        inver += sum(num > num2 for num2 in permuta[i:]) 
    return not inver % 2, inver

p = (7, 2, 6, 3, 5, 4, 1)
p = (3, 2, 1, 4, 5)
p = (4, 2, 3, 1, 5)
print(f"Permutación \n{p}")
bp, ni = esPar(p)
print(f"Inversiones: {ni}")



prinPermuta(3+1)

"""
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)"""