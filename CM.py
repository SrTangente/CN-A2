from os import listdir
import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from distributions import degree_distributions
from networkx.algorithms import *

n = 100
m = 5
x = np.random.poisson(size=100)
stubs = []
for i in range(len(x)):
    stubs.append([i]*x)

net = nx.Graph()

while nx.number_of_nodes(net) < n:
    new_node = nx.number_of_nodes(net)+1
    for i_m in range(m):
        degree_list = np.array([x[1] for x in nx.degree(net)])
        deg_sum = np.sum(degree_list)
        accumulated_deg = [np.sum(degree_list[0:i]) for i in range(0, len(degree_list))]
        rand_to_attach = np.random.random() * deg_sum
        for j in range(0, len(accumulated_deg)-2):
            if accumulated_deg[j] < rand_to_attach < accumulated_deg[j + 1]:
                nx.add_path(net, [j+1, new_node])

if n <= 100:
    nx.draw(net)
degree_distributions(net, apply_log=True)

