import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import csv


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


with open('graficas\\mycsv.csv', 'r') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
 
#print headers
labels=make_label_dict(headers)



mydata = genfromtxt('graficas\\mycsv.csv', delimiter=',')
adjacency = mydata[1:,1:]

print(adjacency)
print(mydata)
print(type(mydata))

"""
labels = {}
labels[0] = 'a'
labels[1] = 'b'
labels[2] = 'c'
labels[3] = 'd'"""
#show_graph_with_labels(adjacency, make_label_dict(get_labels('Graficas\\mycsv.csv')))
show_graph_with_labels(adjacency, labels)

"""mydata = genfromtxt('mouse.csv', delimiter=',')"""


 
"""
input_data = pd.read_csv('data/adjacency_matrix.csv', index_col=0)
#print input_data.head
print input_data.values
G = nx.Graph(input_data.values)"""
 
