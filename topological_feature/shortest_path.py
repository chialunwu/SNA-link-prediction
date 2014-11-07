__author__ = 'bingo4508'
# args[1]: edge_file

import sys
from topological_feature.score import *


def shortest_path(G, li):
    rt = []
    for e in li:
        l = nx.shortest_path_length(G, source=e[0], target=e[1])
        rt.append((e[0], e[1], l))
    return rt


m = SocialNetwork("../data/train_edges.txt")
edge_file = sys.argv[1]

# Shortest path
pair_score(m.G, shortest_path, edge_file, 'output/shortest_path_test.txt')