# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Diagrama de Bifurcación """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D



def lineal(): 
    dom = np.arange(0, 50, 1)

    plt.plot(dom, 2*dom)
    plt.xlabel("Población de la actual generación")
    plt.ylabel("Población de la siguiente generación")
    plt.show()


def Logistico():
    #Modelo logistico
    #Tamaño de la población actual
    #Tasa de nacimiento
    #Tasa de muertes
    #Limite que de población que el habitat soporta

    birdRat = 2
    deatRat = 0.4
    carrCap = 32
    poblIni = 20


    #deatRat = 0.1
    carrCap = 64
    nsig = poblIni
    R = birdRat - deatRat
    for i in range(10):
        plt.plot(i, nsig, "*")
        #xt = nsig / carrCap
        #nsig = R*xt*(1 - xt)
        nsig = R*(carrCap*nsig-nsig**2) / carrCap

    plt.show()


"""
def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
        return a + b


vfunc = np.vectorize(myfunc)
vfunc([1, 2, 3, 4], 3)"""


"""
A unimodal map is a smooth (at least C2) map f:I→Iof an interval 
I⊂R with a unique critical point c∈int I which is a maximum. 
We will also assumethat f(∂I )⊂∂I. The main examples of unimodal maps 
are given by the quadraticfamily of maps pa(x) = a−x2, where −1/4≤a≤2 is a parameter
"""
def FuncSin2M(R, xn):
    """
    0 <= R <= 4   ?
    R*np.sin(xn)
    """
    return R*np.sin(xn)

def FuncSinM(R, xn):
    """0 <= R <= 1 
    R*sin(pi*x)
    """
    return R*np.sin(np.pi*xn)

def FuncSMap(R, xn):
    """
    0< μ ≤ 2 is S-Unimodal map 
    1-R*xn**2
    """
    return 1-R*xn**2

def FuncCuad(R, xn):
    """
    −1/4≤a≤2
    R-x^2
    """
    return R-xn**2

def FuncCuand2(R, xn):
    """
    Simplemente 
    x^2 - 2 
    """
    return xn**2 -2

def FuncMap(R, xn):
    return R*xn*(1-xn)

def TendMap(R, xn):
    """
    Muy interesante esta función
    """
    #print(type(xn))
    #print(f"xn: {xn[0]}")
    #print(f"R: {R}")
    #print(f"val: {R*xn[0]}")
    for i in range(len(xn)):
        if xn[i] < 1/2:
            xn[i] = R[i]*xn[i]
        else:
            xn[i] = R[i]*(1-xn[i])
    return xn

def MapeoLogistico(R, x0, nxs, ven=None, pinta = False, bolita=0):
    x00 = x0
    xs = range(nxs)
    xn = []
    for i in xs:
        xn.append(x0)
        x0 = FuncMap(R, x0)
        
    #x00 = [FuncMap(R, x0)]

    if ven != None:
        #ven.plot(xs, xn, "*")
        ven.plot(xs, xn, marker="o", fillstyle=Line2D.fillStyles[bolita])
        ven.plot(xs, xn)
        ven.set(xlabel='t', ylabel='x(t)')
        ven.set_title(f"R = {R}  x0 = {x00}")
    else:
        if pinta:
            plt.plot(xs, xn, "*")
            plt.plot(xs, xn)
            plt.xlabel("t")
            plt.ylabel("x(t)")
            plt.title(f"R = {R}  x0 = {x00}")
            plt.show()


def MapeoVariosParams():
    """
    Dibuja el mapeo con diferentes parámetros

    dependencia sensible a condiciones iniciales
    three different classes of final behavior (attractors):
    fixed point, periodic and chaotic
    Chaotic attractors are also sometimes called "strange attractors"
    Type atractor is one way in which dynamical systems theory characterizes the 
    behavior of a system

    Chaos se usa para describir sistemas dinámicos con dependencia
    sensible a condiciones iniciales.
    aleatoriedad, impredictibilidad
    """
    # 0.5 punto fijo
    #Permanece en 0.5
    MapeoLogistico(2, 0.5, 21)

    #un poco más interesante
    MapeoLogistico(2, 0.2, 21)

    MapeoLogistico(2, 0.99, 21)


    #fixed point 0.6
    MapeoLogistico(2.5, 0.5, 21)

    #Oscillation, attractor, period = 2
    MapeoLogistico(3.1, 0.2, 81)

    MapeoLogistico(3.4, 0.2, 81)

    #period = 4
    MapeoLogistico(3.49, 0.2, 81)

    MapeoLogistico(3.54, 0.2, 81)

    MapeoLogistico(3.564, 0.2, 101)

    MapeoLogistico(3.5687, 0.2, 121)

    MapeoLogistico(3.569946, 0.2, 121)

    # Chaotic
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
    fig.suptitle(f"Logistic FuncMap")
    MapeoLogistico(2.5, 0.5, 21, ax1)
    MapeoLogistico(3.4, 0.2, 81, ax2)
    MapeoLogistico(3.5687, 0.2, 121, ax3)

    MapeoLogistico(4, 0.2, 161, ax4)
    MapeoLogistico(4, 0.21, 161, ax5, bolita=5)

    MapeoLogistico(4, 0.20000000001, 161, ax6, bolita=1)

    plt.show()


def BifurcacionDiagr(Mapeo=None, Ri=2.5-2.5, Rf=4.0+0.0000001, niter=100, uiter=0, cadMap=None, x0=0.2):
    """
    Dibuja el diagrama de bifurcación
    Para el mapero logístico 
    Dibuja para cada R, la cantidad de puntos fijos

    Por qué sólo en ese intervalo?
    Por qué ese número de iteraciones?
    Por qué sólo las últimas iteraciones?
    """
    n = 10000*5
    r = np.linspace(Ri, Rf, n)

    iterations = niter
    last = uiter
    #x = 1e-5 * np.ones(n)
    #x = 0.2 * np.ones(n)
    x = x0 * np.ones(n)

    #fig, (ax1) = plt.subplots(1, 1, figsize=(8, 9), sharex=True)
    fig, (ax1) = plt.subplots(1, 1, sharex=True)

    for i in range(iterations):
        #x = FuncMap(r, x)
        if Mapeo != None:
            x = Mapeo(r, x)
        # We display the bifurcation diagram.
        if last == 0 or i >= (iterations - last):
            ax1.plot(r, x, ',k', alpha=.25)
            #ax1.plot(r[i:], x[i:], ',c', alpha=.25)

    ax1.set(xlabel='R', ylabel='atractor')
    ax1.set_xlim(Ri-.5, Rf+1)
    ax1.set_title(f"Bifurcation diagram, mapeo: {cadMap}")

    plt.tight_layout()
    plt.show()

def Bifurcacion3DDiagr(Mapeo=None, Ri=2.5-2.5, Rf=4.0+0.0000001, niter=100, uiter=0, cadMap=None):    
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    n = 10000
    r = np.linspace(Ri, Rf, n)

    iterations = niter
    last = uiter
    #x = 1e-5 * np.ones(n)
    x = 0.2 * np.ones(n)

    #fig, (ax1) = plt.subplots(1, 1, figsize=(8, 9), sharex=True)
    # fig, (ax1) = plt.subplots(1, 1, sharex=True)

    for i in range(iterations):
        #x = FuncMap(r, x)
        if Mapeo != None:
            x = Mapeo(r, x)
        # We display the bifurcation diagram.
        if last == 0 or i >= (iterations - last):
            ax.plot(r[i:], x[i:], x[i:], ',k', alpha=.25)

    ax.set(xlabel='R', ylabel='atractor')
    ax.set_xlim(Ri-.5, Rf+1)
    ax.set_title(f"Bifurcation diagram, mapeo: {cadMap}")

    plt.tight_layout()
    plt.show()


def DibujaFuncMap(R=2, Mapeo=None):
    """ 
    Dibuja la función Mapeo Logistico
    Entreo 0 y 1 
    """
    x = np.linspace(0, 1)
    fig, ax = plt.subplots(1, 1)
    if Mapeo != None:
        #ax.plot(x, FuncMap(R, x), 'k')
        ax.plot(x, Mapeo(R, x), 'k')
    plt.show()


#DibujaFuncMap(R=5-3.5, Mapeo=FuncCuad)
#BifurcacionDiagr(Mapeo=FuncCuad, Ri=-1/4, Rf=2, niter=100, cadMap="a-x**2")
#BifurcacionDiagr(Mapeo=FuncSMap, Ri=0, Rf=2, niter=100, uiter=4, cadMap="1-R*x**2")
#BifurcacionDiagr(Mapeo=FuncSinM, Ri=0, Rf=1, niter=100, cadMap="R*sin(pi*x)")
#Bifurcacion3DDiagr(Mapeo=FuncSin2M, Ri=0, Rf=3.1, niter=100, cadMap="R*sin(x)")

#MapeoVariosParams()
#BifurcacionDiagr(Mapeo=FuncCuand2, Ri=-2, Rf=2, niter=100, cadMap="x**2-2", x0=0.1)
BifurcacionDiagr(Mapeo=TendMap, Ri=0, Rf=2, niter=2800, cadMap="Tend Map", x0=0.1, uiter=10)
