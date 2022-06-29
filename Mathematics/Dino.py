
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
p = Polygon(y, facecolor = 'k')

fig, ax = plt.subplots()
ax.add_patch(p)

ax.set_xlim([-7,7])
ax.set_ylim([-7,7])
ax.set_title("A qué se parece, Pythón")
plt.show()