# -*- coding: utf-8 -*-

""" Definir una matriz y calcular su transpuesta 
"""
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"


import numpy as np

def Transpuesta(A):
    print(f"La matriz: \n {A}") 
    print(f"Su transpuesta:\n {A.T}") 

C = np.matrix("1 1 1 1; 1 2 3 4; 0 1 2 3; 0 0 1 2; 0 0 0 1")
T = np.matrix("1 ; 2; 3; 4; 5")

Transpuesta(C)
Transpuesta(T)