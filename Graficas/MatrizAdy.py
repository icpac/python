import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import csv


def show_digraph_with_labels(adjacency_matrix, mylabels, pos):
    ns = adjacency_matrix.shape[1]
    es = adjacency_matrix.shape[0]
    
    DG = nx.DiGraph()
    DG.add_nodes_from(pos.keys())
    for n, p in pos.items():
        DG.nodes[n] ['pos'] = p

    rows, cols = np.where(adjacency_matrix == 1)
    rowsn, colsn = np.where(adjacency_matrix == -1)
    edges = list(zip(cols.tolist(), colsn.tolist()))

    DG.add_edges_from(edges)
    nx.draw(DG, pos, node_size=500, labels =mylabels)
    plt.show()


def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()


def make_label_dict(labels):
    l = {}
    j = 0
    for i, label in enumerate(labels):
        if label: 
            l[i-j] = label
        else:
            j+=1
    return l


def LeeGrafica(nombre):
    with open(nombre, 'r') as f:
        d_reader = csv.DictReader(f)
        headers = d_reader.fieldnames
 
    labels = make_label_dict(headers)

    mydata = genfromtxt(nombre, delimiter=',') #,dtype=None)
    mydata = genfromtxt(nombre, delimiter=',',dtype='U20',
    converters={0:lambda x: x.decode()})
    adjacency = mydata[1:,1:]

    return adjacency, labels
    """
    labels = {}
    labels[0] = 'a'
    labels[1] = 'b'
    labels[2] = 'c'
    labels[3] = 'd'"""
    #show_graph_with_labels(adjacency, make_label_dict(get_labels('Graficas\\mycsv.csv')))
    """mydata = genfromtxt('mouse.csv', delimiter=',')"""
 
    """
    input_data = pd.read_csv('data/adjacency_matrix.csv', index_col=0)
    #print input_data.head
    print input_data.values
    G = nx.Graph(input_data.values)"""

    """
    DG = nx.DiGraph()
    DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
    DG.out_degree(1, weight='weight')
    DG.degree(1, weight='weight')
    list(DG.successors(1))
    list(DG.neighbors(1))
    nx.draw(DG, node_size=500)
    plt.show()
    """

if __name__ == "__main__":
    #MaAdjacency, labels = LeeGrafica('graficas\\mycsv.csv')
    MaAdjacency, labels = LeeGrafica('graficas\\matriz2.csv')
    #pos = {0: (.5, 2), 1: (-.5, 1), 2: (1.5, 1), 
    #3: (0, 0), 4: (1, 0), 5:(), 6:()}  
    
    pos = {}
    r = 1
    ns = MaAdjacency.shape[1]
    for i in range(ns):
        x = r * np.cos(2 * np.pi * i / ns) 
        y = r * np.sin(2 * np.pi * i / ns)
        pos[i] = (x, y)


    #show_graph_with_labels(MaAdjacency, labels)
    show_digraph_with_labels(MaAdjacency, labels, pos)
