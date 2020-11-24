#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from timeit import timeit
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("macosx")


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time: O(V+E) vertices + edges, Space: O(V)
    def depthFirstSearch(self, array):
        array.append(self.name)
        # print("Array is: %s" % array)
        # print("My name is: %s and my children are: %s" % (self.name, self.children))
        for child in self.children:
            child.depthFirstSearch(array)
        return array

    def __repr__(self):
        return f"{self.name} children: %s" % [x.name for x in self.children]


if __name__ == '__main__':
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    timeit(array = graph.depthFirstSearch([]))

    # print("Top of graph: %s" % graph)
    # print("Child 0: %s" % (graph.children[0]))
    # print("Child 1: %s" % (graph.children[1]))
    # print("Child 2: %s" % (graph.children[2]))
    # print("Child 0 child 1: %s" % (graph.children[0].children))
    # print("Child 1 child 1: %s" % (graph.children[1].children))
    # print("Child 2 child 1: %s" % (graph.children[2].children))

    display_graph = {
                    'A': ['D', 'C', 'B'],
                    'B': ['E', 'F'],
                    'C': [],
                    'D': ['G', 'H'],
                    'E': [],
                    'F': ['I', 'J'],
                    'G': ['K']}

    assert array == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"], "Returned array was incorrect"
    print(array)
    G = nx.Graph(display_graph)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()
