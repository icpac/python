# -*- coding: utf-8 -*-

__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

""" Proceso de otrogonalización Gram Schmidt """ 

import numpy as np
import matplotlib.pyplot as plt


def GramS(vectors):
    """ Calcula vectores ortonormales """
    ortnor = vectors.copy()
    norm1 = np.linalg.norm(ortnor[0])
    if norm1 > 0:
        ortnor[0] = ortnor[0]*(1/norm1)

    for k in range(1, len(ortnor)):
        for j in range(k, len(ortnor)):
            dot = np.dot(ortnor[k-1], ortnor[j])
            ortnor[j] = ortnor[j] - dot*ortnor[k-1]
    
        normk = np.linalg.norm(ortnor[k])
        if normk > 0:
            ortnor[k] = ortnor[k]*(1/normk)

    return ortnor

def dibujaVectores(ortnor):
    """ Dibuja los vecotres 2D """
    # origin point
    origin = np.array([[0, 0],[0, 0]]) 

    plt.quiver(*origin, vectors[:,0], vectors[:,1], color=['g','g'], scale=5, label="Originales")
    plt.quiver(*origin, ortnor[:,0], ortnor[:,1], color=['r','b'], scale=5, label="Ortonormales")
    plt.title("Gram-Schmidt")
    plt.legend()
    #plt.axis('off')
    plt.show()

def dibujaVectores3d(ortnor):
    """Dibuja los vectores 3D """
    # origin point
    origin = np.array([[0, 0, 0],[0, 0, 0], [0, 0, 0]]) 

    print("Ori:", *origin)
    print("Ori:", origin[0])
    print("Vect: ", vectors[:, 0])
    print("Vect: ", vectors[:, 1])
    print("Vect: ", vectors[:, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.quiver([0, 0, 0], [0, 0, 0], [0, 0, 0], vectors[0], vectors[1], vectors[2])
    #plt.quiver(*origin, vectors[:,0], vectors[:,1], vectors[:,2], color=['g','g','g'], scale=5, label="Originales")
    #plt.quiver(*origin, ortnor[:,0], ortnor[:,1], ortnor[:,2], color=['r','b','r'], scale=5, label="Ortonormales")
    plt.title("Gram-Schmidt")
    plt.legend()
    #plt.axis('off')
    plt.show()

def norma(vectors):
    norms = []
    for vec in vectors:
        norms.append(np.linalg.norm(vec))
    return norms

def puntoDosDos(vectors):
    u=1
    punt = []
    for vec1 in vectors:
        for vec2 in vectors[u:]:
            punt.append(np.round(np.vdot(vec1, vec2), 0))
        u+=1

    return punt

vectors = np.array([[-1., 1.5], [2., 0.]])
print(vectors)
#vectors = np.array([[2., 1, 1], [1., 0., 10.], [2., -3., 11.]])


nv = int(input("Cuantos vectores: "))
vct = []
for i in range(0,nv):  
   vct.append([float(j) for j in input().split()]) 

vectors = np.array(vct)
print(vectors)

ortonor = GramS(vectors)
norms = norma(ortonor)
punts = puntoDosDos(ortonor)

print(ortonor)
print(norms)
print(punts)

dibujaVectores(ortonor)
#dibujaVectores3d(ortonor)