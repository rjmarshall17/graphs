#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pylab as plt

graph = {'A': ['D', 'C', 'B'],
         'B': 'E',
         'C': ['G', 'F'],
         'D': ['H'],
         'E': ['I'],
         'F': ['J']}


# Time: O(V+E), space: O(V)
def breadthFirstSearch(graph, source):
    array = []
    queue = [source]
    while len(queue) > 0:
        s = queue.pop(0)
        array.append(s)
        if s not in graph:
            continue
        if len(graph[s]) > 0:
            for child in reversed(graph[s]):
                queue.append(child)
    return array


if __name__ == '__main__':
    results = breadthFirstSearch(graph, "A")
    print(results)
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()
