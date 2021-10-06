# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Pensé que saldría algo chido pero parece que no  """ 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def DibujaParale(ax, A, C, clr):
    ax.plot([0, A[0]], [0, A[1]], color=clr)
    ax.plot([0, C[0]], [0, C[1]], color=clr)
    
    ax.plot([A[0], A[0]+C[0]], [A[1], A[1]+C[1]], color=clr)
    ax.plot([C[0], A[0]+C[0]], [C[1], A[1]+C[1]], color=clr)

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


def ParesFibonacci():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    """
    F0 = 0
    F1 = 1
    Fn+1 = Fn + Fn-1

    nesimo
    A = fn-1, fn
    BC = fn, Fn+1"""

    n = 3
    clr = 'blue'
    while n < 5:
        DibujaParale(ax, [Fibonacci(n-1), Fibonacci(n)], [Fibonacci(n), Fibonacci(n+1)], clr)
        clr = 'red'
        n=n+1

    plt.show()


def SumsParcCuadFibona(n):
    return Fibonacci(n-1)**2 + Fibonacci(n)**2


def ImprimeSumasParc(hasta=3):
    n = 1
    while n < hasta:
        print(f"n: {SumsParcCuadFibona(n)}")
        n+=1


ImprimeSumasParc(hasta=6)
ParesFibonacci()
