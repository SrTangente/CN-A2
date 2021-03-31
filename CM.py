from os import listdir
import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from distributions import degree_distributions
from networkx.algorithms import *

# size
n = 100
x = np.random.poisson(size=n)

nodes_stubs = {}
stubs = []

j = 0
for i in range(len(x)):
    nodes_stubs[i] = []
    for k in range(x[i]):
        j += 1
        nodes_stubs[i].append(j)
        stubs.append(i)

# number of stubs must be even
if np.sum(stubs) % 2 != 0:
    x[-1] += 1
    stubs.append(n-1)

print(x)
print(stubs)
print(nodes_stubs)

net = nx.Graph()

while len(stubs) > 0:
    rnd_stub_index = int(np.random.random()*len(stubs))
    rnd_stub = stubs[rnd_stub_index]
    degree_list = np.array([x[1] for x in nx.degree(net)])
    deg_sum = np.sum(degree_list)
    accumulated_deg = [np.sum(degree_list[0:i]) for i in range(0, len(degree_list))]
    rand_to_attach = np.random.random() * deg_sum
    for j in range(0, len(accumulated_deg)-2):
        if accumulated_deg[j] < rand_to_attach < accumulated_deg[j + 1]:
            internal_stub_index = int(rand_to_attach - accumulated_deg[j])
            selected_stub = nodes_stubs[j][internal_stub_index]

            if rnd_stub != selected_stub and not net.has_edge(rnd_stub, selected_stub):
                stubs = np.delete(stubs, rnd_stub_index)
                stubs = np.delete(stubs, selected_stub)
                nodes_stubs[j].remove(internal_stub_index)
                nx.add_path(net, [rnd_stub, selected_stub])
                break


if n <= 100:
    nx.draw(net)
degree_distributions(net, apply_log=True)

