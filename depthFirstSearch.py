#!/usr/bin/env python3
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


# Time: O(V+E) vertices + edges, Space: O(V)
def depthFirstSearch(graph, source):
    stack = [source]
    array = []
    while len(stack) > 0:
        # print("Current stack: %s" % stack)
        s = stack.pop()
        # print("Popped: %s" % s)
        # If s is not in the graph, i.e. not a key/parent only a child, add it to the array
        if s not in graph:
            # print("s (%s) was not in the graph %s" % (s,graph))
            array.append(s)
        if s not in array:
            array.append(s)
            # s is a key in the graph, and has neighbors/children
            for c in graph[s]:
                stack.append(c)
                # print('Appended to stack: %s' % c)
    # 		else:
    # 			print("%s was in array" % s)
    return array


if __name__ == '__main__':
    result = depthFirstSearch(graph, 'A')
    assert result == CORRECT_ORDER, "Incorrect order for return: %s" % result
    print(result)
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()
