

__autor__= "Tlacaelel Icpac"
__email__= "tlacaelel.icpac@gmail.com"

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x0Act = 0
a = -.1
b = 1.15 
x = np.arange(a, b, 0.1)
x0s = [.1, .3, .5, .8]
funcion = lambda t: 4*t *(1-t)
#funcion = lambda t: t**2 - 1.1
#funcion = lambda t: 2*t * (1-t)
#dos listas para los puntos de la órbita
xdata, ydata = [], []


#dibujamos la órbita
x0 = -.2
limItera = 200
itera = 0

"""
while itera < limItera:
    if itera % 2 == 0:     
        xdata.append(x0)
        ydata.append(x0)
    else:
        xdata.append(x0)
        ydata.append(funcion(x0))
        x0 = funcion(x0)
    itera += 1"""


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.plot(x, funcion(x), color="green")
ax.plot(x, x, color="blue")
#Dibuja la telaraña
#ax.plot(xdata, ydata)

#cuadricula
ax.grid()
#eje x
ax.axhline(y = 0, color='k')
#eje y
ax. axvline(x = 0, color = 'k')

def init():
    global x0s, x0Act, x0
    del xdata[:]
    del ydata[:]
    if len(x0s) > x0Act:
        x0 = x0s[x0Act]
        x0Act += 1
        
    line.set_data(xdata, ydata)
    return line

def data_gen():
    global x0, limItera, a, b
    itera = 0
    while itera < limItera and (x0 > a and x0 < b):
        if itera % 2 == 0:     
            yield x0, x0
        else:
            yield x0, funcion(x0)
            x0 = funcion(x0)
        itera += 1

def run(data):
    x, y = data
    xdata.append(x)
    ydata.append(y)

    line.set_data(xdata, ydata)
    return line
    
ani = animation.FuncAnimation(fig, run, data_gen, interval=20, repeat=True,
                              init_func=init)
plt.show()
