# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pylab as plt

graph = {'A': ['D', 'C', 'B'],
         'B': 'E',
         'C': ['G', 'F'],
         'D': ['H'],
         'E': ['I'],
         'F': ['J']}

G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)


def breadthFirstSearch(graph, source):
    array = []
    stack = [source]
    while len(stack) > 0:
        s = stack.pop(0)
        array.append(s)
        if s not in graph:
            continue
        if len(graph[s]) > 0:
            for child in reversed(graph[s]):
                stack.append(child)
    return array


if __name__ == '__main__':
    results = breadthFirstSearch(graph, "A")
    print(results)
