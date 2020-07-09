
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dinamicos:
    def __init__(self):
        self.x0Act = 0
        self.limItera = 15
        self.xdata, self.ydata = [], []
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)


    def grafFuncion(self, f, domf, pts, ax1):
        #pinto la identidad
        ax1.plot(domf, domf)
        #pinto la función
        ax1.plot(domf, f(domf))

        if len(pts) > 0:
            ax1.plot(pts, pts, 'o', color='black')

        ax1.grid(True, which='both')
        #eje x
        ax1.axhline(y=0, color='k')
        #eje y
        ax1.axvline(x=0, color='k')

    def init(self):
        del self.xdata[:]
        del self.ydata[:]

        if len(self.x0s) > self.x0Act:
            self.x0 = self.x0s[self.x0Act]
            self.x0Act += 1
        else:
            self.x0Act = 0
            self.x0 = self.x0s[self.x0Act]

        self.line.set_data(self.xdata, self.ydata)
        return self.line

    def data_gen(self):
        self.itera = 0
        while self.itera < self.limItera and (self.x0 > self.a and self.x0 < self.b):
            if self.itera % 2 == 0:     
                yield self.x0, self.x0
            else:
                yield self.x0, self.f(self.x0)
                self.x0 = self.f(self.x0)
            self.itera += 1

    def run(self, data):
        x, y = data
        self.xdata.append(x)
        self.ydata.append(y)

        self.line.set_data(self.xdata, self.ydata)
        return self.line


    def puntosFijos(self, expr):
        t = symbols('t', real = True)
        
        pts = solve(expr - t)
        print("Puntos fijos de: " + str(expr) + ", son: " + str(pts))

    def tipoFijo(self, expr):
        t = symbols('t', real = True)

        pts = solve(expr - t)
        exprD = diff(expr, t)
        print("La derivada es: ", exprD)
        DerivativeOfF = lambdify((t), exprD,"numpy")
        for i in range(len(pts)):
            print("El valor de la derivada en: "+ str(pts[i]) +
                  ", es: " + str(DerivativeOfF(pts[i])))

    def animate(self, expr, xi, xf, xs):
        self.a = xi
        self.b = xf
        self.xd = np.arange(self.a, self.b, 0.1)
        self.x0s = xs
        
        t = symbols('t', real = True)
        pts = solve(expr - t)

        self.f = lambdify(t, expr)
        self.grafFuncion(self.f, self.xd, pts, self.ax)
        self.ax.plot(self.xd, self.f(self.xd), color="green")
        self.ax.plot(self.xd, self.xd, color="blue")

        ani = animation.FuncAnimation(self.fig, self.run, self.data_gen,
                interval=290, repeat=True, init_func=self.init)
        plt.show()


t = symbols('t', real = True)

"""
x0s = [.89, .95, 1.03, 1.05]"""
d = Dinamicos()
expr = 1/t**2
"""
d.puntosFijos(expr)
d.tipoFijo(expr)
d.animate(expr, 0.47, 2.3, x0s)

fig, ax = plt.subplots()
d.grafFuncion(lambdify(t, expr), np.arange(.1, 1, 0.01), [], ax)
plt.show()"""


d = Dinamicos()
expr = t**4 - 4*t**2 + 2
d.puntosFijos(expr)
d.tipoFijo(expr)
x0s = [-1.01, -1.09, -0.911, -0.979]
d.animate(expr, -4, 2, x0s)

"""
d = Dinamicos()
x0s = [1.98, 1.97, 2.001, 2.0009] # 2
d.animate(expr, 1, 2.7, x0s)

d = Dinamicos()
x0s = [-1.601, -1.6009, -1.509, -1.5009] #-1.618
d.animate(expr, -2.618, -0.618, x0s)"""

d = Dinamicos()
x0s = [.61, .6, .63, .64] # .618,
d.animate(expr, -0.381, 1.618, x0s)

fig, ax = plt.subplots()
d.grafFuncion(lambdify(t, expr), np.arange(-3, 3, 0.1), [], ax)
plt.show()

