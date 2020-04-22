"""
Tlacaelel Icpac
tlacaelel.icpac@gmail.com

Toma datos aleatorios, y según su valor los coloca
en alguno de los tres triángulos.

"""
import numpy as np
import matplotlib.pyplot as plt


tres_vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(.75)]])
datos = np.random.uniform(-1, 1, 600)
medios = np.zeros(len(datos))

i = 0
j = 0
#Media entre dos datos consecutivos
while j+1 < len(datos):
    medios[i] = (datos[j] + datos[j+1])/ 2
    j += 1
    i += 1

#Valor máximo y minimo de los datos
maximo = max(medios)
minimo = min(medios) 

medios.sort()

tercio = (maximo - minimo) / 3

pmy11 = np.sqrt(.75) / 2

pt1 = pmy11 / 0.25

plt.plot([0, 0.5,          1, 0, 0.25, 0.5, 0.75, 0.25],
         [0, np.sqrt(.75), 0, 0, pmy11, 0, pmy11, pmy11])
j = 0
while j < len(medios):
    if medios[j] < minimo + tercio:
        x1 = np.random.uniform(0, 0.5, 1)
        if x1 < 0.25:
            y1 = np.random.uniform(0, pt1*x1, 1)
        else:
            y1 = np.random.uniform(0, -pt1*(x1-0.5), 1)
    elif  minimo + tercio <= medios[j] < minimo + 2*tercio:
        x1 = np.random.uniform(0.25, 0.75, 1)
        if x1 < 0.5:
            y1 = np.random.uniform(pmy11, pt1*x1, 1)
        else:
            y1 = np.random.uniform(pmy11, -pt1*(x1-1), 1)
    else:
        x1 = np.random.uniform(0.5, 1, 1)
        if x1 < 0.75:
            y1 = np.random.uniform(0, pt1*(x1-0.5), 1)
        else:
            y1 = np.random.uniform(0, -pt1*(x1-1), 1)

    plt.plot(x1, y1, 'o')
    j += 1

    
plt.show()    


