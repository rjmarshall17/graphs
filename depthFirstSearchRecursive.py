# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pylab as plt

class Node:
    def __init__(self,name):
        self.children = []
        self.name = name
        
    def addChild(self,name):
        self.children.append(Node(name))
        return self
        
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

    def __repr__(self):
        return f"{self.name} children: %s" % [x.name for x in self.children]

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
array = graph.depthFirstSearch([])
assert array == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],"Returned array was incorrect"
print(array)