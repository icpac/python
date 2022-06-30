
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
#from vector_drawing import *

def greet(name):
    print("Hello %s!" % name)
    
def string():    
    for name in ["John","Paul","George","Ringo"]:
        greet(name)


def Draw(vectors):
    Polygon(vectors)

y = [(1,2), [-1,5], [-2,5], [-3,4], 
    [-4,4], [-5, 3], [-5, 2], [-2, 2], [-5, 1],
    [-4, 0], [-2, 1], [-1, 0], [0, -3], [-1, -4],
    [1, -4], [2, -3], [1, -2], [3, -1],
    [5, 1], [6, 4], [3, 1], [1, 2]]

def DinoSegmen(y):
    xs = [l[0] for l in y]
    ys = [l[1] for l in y]
    xs, ys = zip(*y)

    for i in range(0, len(y)):
        x1, y1 = y[i]
        x2, y2 = y[(i+1)%(len(y))]
        plt.plot([x1, x2], [y1, y2], color="blue")

    #plt.scatter(xs, ys)





def DrawDino():
    p = Polygon(y, facecolor = 'k')

    fig, ax = plt.subplots()
    ax.add_patch(p)
    ax.set_xlim([-7,7])
    ax.set_ylim([-7,7])
    ax.set_title("A qué se parece, Pythón")
    plt.show()

def uno():
    lp = [[1,2], [-1,5], [-2,5], [-3,4]]
    print(type(lp)) 
    print(type([(1,2), (-1,5), (-2,5), (-3,4)])) 

    print(lp)
    print(type(*lp))
    for j in lp:
        print(j)


def dos():
    lcua = [(x, x**2) for x in range (-10, 11)]

    xs = [l[0] for l in lcua]
    ys = [l[1] for l in lcua]
    plt.scatter(xs, ys)
    plt.show()

def tres():
    #Si lo trato de ver como vectores
    #Los agrega como listas
    v1 = [1, 1]
    v2 = [2,2]
    print(v1+v2)

    v1= (1, 1)
    v2=(2, 2)
    print(v1+v2)
    print((v1[0]+v2[0], v1[1]+v2[1]))

def suma(x, y):
    return [x[0]+y[0], x[1]+y[1]]

def Traslada(r, vectors):
    return [suma(r, v) for v in vectors]

def Escala(esca, vector):
    return (esca * vector[0], esca*vector[1])

#DinoSegmen(y)
#DinoSegmen(Traslada([1,1], y))
for i in range(0, 20, 2):
    for j in range(0, 20, 2):
        ey = [Escala(1/5, v) for v in y]
        et = Traslada((j, i), ey)
        #et = Traslada((j, i), y)
        DinoSegmen(et)

plt.title("Qué figura hay ahí?")
plt.show()
