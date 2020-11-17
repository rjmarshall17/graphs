# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("macosx")

graph = {'A': ['D', 'C', 'B'],
         'B': ['E'],
         'C': ['G', 'F'],
         'D': ['H'],
         'E': ['I'],
         'F': ['J']}

CORRECT_ORDER = ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']


def depthFirstSearch(graph, source):
    stack = [source]
    array = []
    while len(stack) > 0:
        # 		print("Current stack: %s" % stack)
        s = stack.pop()
        # 		print("Popped: %s" % s)
        if s not in graph:
            array.append(s)
        if s not in array:
            array.append(s)
            for c in graph[s]:
                stack.append(c)
    # 		else:
    # 			print("%s was in array" % s)
    return array


G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)


if __name__ == '__main__':
    result = depthFirstSearch(graph, 'A')
    assert result == CORRECT_ORDER, "Incorrect order for return: %s" % result
    print(result)
