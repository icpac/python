"""
Tlacaelel Icpac
tlacaelel.icpac@gmail.com

Gráfica de la república con algunas medidas de centralidad
"""

import networkx as nx
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np


__author__ = "Tlacaelel Icpac"
__credits__ = ["Tlacaelel Icpac"]
__version__ = "1.0"
__email__ = "tlacaelel.icpac@gmail.com"


#interactivo
#plt.ion()

#1 Baja California
#2 Baja California Sur
#3 Sonora
#4 Chihuahua
#0 Sinaloa
#6 Durango
#7 Coahuila
#8 Nayarit
#9 Jalisco
#10 Zacatecas
#11 San Luis Potosi
#12 Nuevo León
#13 Colima
#14 Michoacan
#15 Guanajuato
#16 Aguascalientes
#17 Queretaro
#18 Hidalgo
#19 Veracruz
#20 Tamaulipas
#21 Estado de México
#22 Tlaxcala
#23 Puebla
#24 Oaxaca
#25 Chiapas
#26 Tabasco
#27 Guerrero
#28 Morelos
#29 Ciudad de Mexico
#30 Campeche
#31 Yucatán
#32 Quintana Roo

g = nx.Graph()
#Estados o ciudades y sus posiciones
g.add_node('BC1', pos=(-2, 36))
g.add_node('BS2', pos=(6, 20))
g.add_node('SN3', pos=(8, 31))
g.add_node('CH4', pos=(15, 29))
g.add_node('SI5', pos=(13, 21))
g.add_node('DR6', pos=(19, 21))
g.add_node('CO7', pos=(23, 27))
g.add_node('NY8', pos=(18, 15))
g.add_node('JL9', pos=(20, 12))
g.add_node('ZC10', pos=(23, 19))
g.add_node('SN11', pos=(26.5, 18))
g.add_node('NL12', pos=(29, 23))
g.add_node('CL13', pos=(20, 10))
g.add_node('MC14', pos=(25, 10))
g.add_node('GT15', pos=(26, 14))
g.add_node('AG16', pos=(23, 16))
g.add_node('QR17', pos=(29, 13.2))
g.add_node('HG18', pos=(31, 12.5))
g.add_node('VR19', pos=(38, 9))
g.add_node('TM20', pos=(32, 20))
g.add_node('ED21', pos=(29, 10.5))
g.add_node('TX22', pos=(32, 11))
g.add_node('PB23', pos=(34, 9.5))
g.add_node('OX24', pos=(36, 6))
g.add_node('CP25', pos=(45, 5))
g.add_node('TB26', pos=(44, 9))
g.add_node('GR27', pos=(29.5, 7))
g.add_node('MR28', pos=(30.5, 9.5))
g.add_node('CD29', pos=(30.5, 11))
g.add_node('CM30', pos=(50, 10))
g.add_node('YC31', pos=(53, 14))
g.add_node('QR32', pos=(55, 12))

#aristas de los estados colindantes, con su distancia entre ciudades
g.add_edge('BC1', 'SN3', weight=693) #mex herm
g.add_edge('SN3', 'CH4', weight=880) #herm chih
g.add_edge('SN3', 'SI5', weight=695) #herm cul
g.add_edge('CH4', 'SI5', weight=1138) #chih cul
g.add_edge('CH4', 'CO7', weight=745) #chih salt
g.add_edge('SI5', 'DR6', weight=460) #cul dur
g.add_edge('CH4', 'DR6', weight=688) #chih dur
g.add_edge('SI5', 'NY8', weight=480) #cul tep
g.add_edge('DR6', 'NY8', weight=459) #dur tep
g.add_edge('DR6', 'JL9', weight=666) #dur guada
g.add_edge('DR6', 'CO7', weight=528) #dur salt
g.add_edge('DR6', 'ZC10', weight=301) #dur zac
g.add_edge('BC1', 'BS2', weight=1635) #mex la pa
g.add_edge('CO7', 'ZC10', weight=366) #salt zaca
g.add_edge('CO7', 'SN11', weight=448) #salt san luis
g.add_edge('CO7', 'NL12', weight=70) #salt mont
g.add_edge('NY8', 'JL9', weight=206) #tepc guadal
g.add_edge('NY8', 'ZC10', weight=563) #tep zac
g.add_edge('JL9', 'ZC10', weight=362) #guad zaca
g.add_edge('JL9', 'SN11', weight=359) #guada san luis
g.add_edge('JL9', 'CL13', weight=194) #guada col
g.add_edge('JL9', 'MC14', weight=287) #guada mor
g.add_edge('JL9', 'GT15', weight=284) #guada guana
g.add_edge('JL9', 'AG16', weight=236) #guada aguas
g.add_edge('ZC10', 'SN11', weight=192) #zac san 
g.add_edge('ZC10', 'NL12', weight=439) #zac monte
g.add_edge('ZC10', 'GT15', weight=310) #zac guana
g.add_edge('ZC10', 'AG16', weight=125) #zac aguas
g.add_edge('SN11', 'NL12', weight=501) # san lu monte
g.add_edge('SN11', 'GT15', weight=187) #san luis guana
g.add_edge('SN11', 'QR17', weight=204) #san luis queret
g.add_edge('SN11', 'HG18', weight=419) #san luis pach
g.add_edge('SN11', 'VR19', weight=715) #san luis xalap
g.add_edge('SN11', 'TM20', weight=323) #san luis vict
g.add_edge('NL12', 'TM20', weight=324) # mont vct
g.add_edge('CL13', 'MC14', weight=476) # colima mor
g.add_edge('MC14', 'GT15', weight=178) # more guana
g.add_edge('MC14', 'QR17', weight=188) # more quere
g.add_edge('GT15', 'QR17', weight=148) #guana quere
g.add_edge('QR17', 'HG18', weight=224) #queret pach
g.add_edge('QR17', 'ED21', weight=187) #queret tolc
g.add_edge('HG18', 'VR19', weight=313) #pach xala
g.add_edge('HG18', 'ED21', weight=183) # pach toluc
g.add_edge('HG18', 'TX22', weight=128) #pach tlax
g.add_edge('HG18', 'PB23', weight=142) # pach puebl
g.add_edge('VR19', 'TM20', weight=709) #xala vcto
g.add_edge('VR19', 'PB23', weight=180) #xala puebl
g.add_edge('VR19', 'OX24', weight=451) #xala oax 
g.add_edge('VR19', 'CP25', weight=652) # xalapa tux 
g.add_edge('VR19', 'TB26', weight=562) # xalap villa
g.add_edge('ED21', 'MC14', weight=229) #tolu more
g.add_edge('ED21', 'TX22', weight=191) # toluc tlax
g.add_edge('ED21', 'PB23', weight=197) #toluc publ
g.add_edge('ED21', 'GR27', weight=298) # toluc chilp
g.add_edge('ED21', 'MR28', weight=110) # toluc cuan
g.add_edge('ED21', 'CD29', weight=70) #toluc zoca
g.add_edge('TX22', 'PB23', weight=37) # tlax pueb
g.add_edge('PB23', 'OX24', weight=344) # pub oax
g.add_edge('PB23', 'GR27', weight=315) #pueb chilp
g.add_edge('PB23', 'MR28', weight=142) #pueb cuau
g.add_edge('OX24', 'CP25', weight=567) #oax tux 
g.add_edge('OX24', 'GR27', weight=659) #oax chilp 
g.add_edge('CP25', 'TB26', weight=251) #tux vill
g.add_edge('TB26', 'CM30', weight=382) #vill camp 
g.add_edge('GR27', 'MR28', weight=175) #chilp cuau
g.add_edge('GR27', 'MC14', weight=523) #chilp more
g.add_edge('MR28', 'CD29', weight=88) #cuahu zocal
g.add_edge('CM30', 'YC31', weight=158) #camp meri
g.add_edge('CM30', 'QR32', weight=379) #camp chet
g.add_edge('YC31', 'QR32', weight=382) #mer chet


#dibujamos la gráfica
img = plt.imread("mapa.png")

pos = nx.get_node_attributes(g, 'pos')
plt.grid(True)
#plt.subplot(211)
plt.title("Gráfica, ciudades capitales de los estados de México")
plt.imshow(img, zorder=0, extent=[-10, 58.0, 1.0, 40.0])
nx.draw(g, pos, with_labels=True)

list_edges = list(g.edges())
edge_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
nx.draw_networkx_edge_labels(g, pos=pos, edgelist=list_edges, edge_labels=edge_labels)
plt.axis('off')

plt.show()
#distribución de grados
#p = plt.subplot(212)
plt.xlabel('grados')
plt.ylabel('cantidad')
plt.title("Distribución de grados")
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

grados = g.degree();
grdAct = 0
cnto = 0
for i in range(g.number_of_nodes()+1):
    for n in grados:
        if grdAct == n[1]:
            cnto += 1

    if cnto > 0:
        plt.plot(grdAct, cnto, 'o')
    grdAct += 1
    cnto = 0

def medidasCentralidad():
    global g
    print("Medidas de centralidad:")
    # Excentricidad de un nodo, es la máxima distancia
    # del nodo a todos los demás nodos.
    # La máxima excentricidad
    de = nx.eccentricity(g)
    print("Diámetro de la gráfica:", nx.diameter(g, de))
    # La mínima excentricidad
    print("El radio de la gráfica:", nx.radius(g, de))
    print("")
    # El centro de la gráfica
    # Excentricidad igual al radio
    print("Los centros de la gráfica son: ", nx.center(g))
    for n in nx.center(g):
        print(f"Excentricidad: {n}, {nx.eccentricity(g, n)}")
    # Periferia de la gráfica
    print("")
    print("La periferia de la gráfica: ", nx.periphery(g))
    for n in nx.periphery(g):
        print(f"Excentricidad: {n}, {nx.eccentricity(g, n)}")    
    print("")

    # Cercanía; el recíproco del promedio de las distancias
    # más cortas del nodo a los demás nodos
    print("Centralidad según networkx")
    # C(u) = {n-1} over {sum from{v = 1} to {n-1} {d(u, v)}}
    cnt = nx.algorithms.centrality.closeness_centrality(g)
    print("Nodo \t Centralidad\n Considerando el número de aristas")
    for c in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo: {c}")

    cnt = nx.algorithms.centrality.closeness_centrality(g, distance="weight")
    print("Nodo \t Centralidad\n Considerando la distancia")
    for c in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo: {c}")

    numNodos = g.number_of_nodes()    
    print("\nCentralidad según el libro")
    # g_{i} = 1 over {sum from {j <> i} {l_{ij}}} 
    cnt = nx.algorithms.centrality.closeness_centrality(g)
    print("Nodo \t Centralidad\n Considerando el número de aristas")
    for (c, v) in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        cnt[c] = v/ (numNodos-1)
    for c in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo: {c}")

    cnt = nx.algorithms.centrality.closeness_centrality(g, distance="weight")
    for (c, v) in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        cnt[c] = v/ (numNodos-1)
    print("Nodo \t Centralidad\n Considerando la distancia")
    for c in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo: {c}")    

    betw = nx.algorithms.centrality.betweenness_centrality(g)
    print("\nIntermediación:\n ")
    # b_{i} = sum from{ h <> j <> i} {sigma_{hj}(i)} over {sigma_{hj}}
    for b in sorted(betw.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo: {b}")        
    
    print("")
    
    
    
    

#Matriz de adyacencias
nodos_ordenados = np.sort(g.nodes())
print("Matriz de adyacencias:")
print(nx.to_numpy_matrix(g, nodelist=nodos_ordenados))
A = nx.adjacency_matrix(g)
print(A.todense())

#Nodos de la gráfica
print("")
print("Nodos de la gráfica:")
print(g.nodes)
print("")
medidasCentralidad()

sp = dict(nx.all_pairs_shortest_path(g))
print("Camino para llegar de una ciudad a otra, Baja Sur a Yucatán;")
#orig = str(input("Ciudad Origen: "))
#dstn = str(input("Ciudad Destino: "))
orig = "BS2"
dstn = "YC31"

print("Ruta a seguir: ")
print(sp[orig][dstn])
print("La distancia más corta entre los nodos")
length=dict(nx.all_pairs_dijkstra_path_length(g))
print(str(length[orig][dstn]) + " km" )

plt.show()
