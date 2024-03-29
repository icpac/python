
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def sierpinski(triangulo):
    """toma un triángulo y devuelve 3
    Por ejemplo del original, los
    nuevos vértices serán:
    un vértice original y los puntos medios 
    de los otros lados.
    """
    a, b, c = triangulo
    ab = (a+b)/2
    ca = (c+a)/2
    bc = (b+c)/2
    return ((a, ab, ca),
            (ab, b, bc),
            (ca, bc, c))


""" Triángulo equilátero inicial, de lados 1  """
s = [(np.array([0, 0]),
      np.array([1, 0]),
      np.array([1/2, (1-(1/2)**2)**(1/2)]),
      )]


""" Calculamos los vértices """
iteraciones = 5
for _ in range(iteraciones):
    nuevo_s = []
    for triangulo in s:
        nuevo_s.extend(sierpinski(triangulo))
    s = nuevo_s


""" Se dibuja el triángulo """
f, ax = plt.subplots(1)
for t in s:
    ax.add_patch(Polygon(t))
plt.show()
