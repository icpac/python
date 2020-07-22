
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import matplotlib.pyplot as plt


class Cantor:
    def Grafica(self, pi, pf, nivel):
        xd = [pi, pf]
        yd = [1/nivel, 1/nivel]
        plt.plot(xd, yd, linewidth=2, color='blue')

        puntos = []
        incre = (1/3) ** nivel
        puntos.append([pi, pi+incre])
        puntos.append([pf-incre, pf])
        return puntos

    def Dibuja(self, nivel):
        puntos = []
        puntos.append([0, 1])
        for i in range(nivel):
            nvsP = []
            for pdz in puntos:
                nvsP.extend(self.Grafica(pdz[0], pdz[1], i+1))
            puntos = nvsP

        plt.show()


cnt = Cantor()
cnt.Dibuja(7)

        

"""
def graficaCantor(pi, pf, nivel):
    puntos = []
    #la parte izquierda
    incre = (1/3)** nivel
    xs = [pi, pi+incre]
    ys = [1/(nivel+1), 1/(nivel+1)]
    plt.plot(xs, ys, linewidth=5, color='orange')
    puntos.append(xs)
    
    #parte derecha
    xs = [pf-incre, pf]
    plt.plot(xs, ys, linewidth=5, color='orange')
    puntos.append(xs)
    return puntos

puntos = [[0, 1]]
graficaCantor(0, 1, 0)
for i in range(6):
    nvsP = []
    for pdz in puntos:
        nvsP.extend(graficaCantor(pdz[0], pdz[1], i))
    puntos = nvsP
plt.show()"""

"""
graficaCantor(0, 1, 1)
graficaCantor(0, 1/3, 2)
graficaCantor(2/3, 1, 2)

graficaCantor(0, 1/9, 3)
graficaCantor(2/9, 3/9, 3)
graficaCantor(6/9, 7/9, 3)
graficaCantor(8/9, 1, 3)"""




"""
xs = [0, 1]
ys = [1, 1]
plt.plot(xs, ys, linewidth=10, color='orange')



xs = [0, 1/3]
ys = [1/2, 1/2]
plt.plot(xs, ys, linewidth=10, color='orange')

xs = [2/3, 1]
ys = [1/2, 1/2]
plt.plot(xs, ys, linewidth=10, color='orange')



xs = [0, 1/9]
ys = [1/3, 1/3]
plt.plot(xs, ys, linewidth=10, color='orange')

xs = [2/9, 3/9]
ys = [1/3, 1/3]
plt.plot(xs, ys, linewidth=10, color='orange')

xs = [6/9, 7/9]
ys = [1/3, 1/3]
plt.plot(xs, ys, linewidth=10, color='orange')

xs = [8/9, 1]
ys = [1/3, 1/3]
plt.plot(xs, ys, linewidth=10, color='orange')

plt.show()"""
