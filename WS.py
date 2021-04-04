from os import listdir
import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from distributions import degree_distributions
from networkx.algorithms import *

# size
n = 10000
# medium degree
k = 4
# rewiring probability
p = 0.5

initial_edges = []
#initially we have a ring
for r in range(1, k//2 + 1):
    initial_edges = initial_edges + [(i, i+r) for i in range(n-r)]
    initial_edges.append((n-r, 0))

net = nx.Graph(initial_edges)

for node in net.nodes:
    rnd = np.random.random()
    # each node will be rewired with a small probability
    if rnd <= p:
        new_dest = node
        # only if there is no edge and without self cycles
        while new_dest == node or net.has_edge(new_dest, node):
            new_dest = int(np.random.random() * n)
        net.add_edge(node, new_dest)

if n <= 100:
    nx.draw(net)

degree_distributions(net, apply_log=False)
nx.write_pajek(net, './networks/BA_'+str(n)+'_'+str(k)+'_'+str(p))
