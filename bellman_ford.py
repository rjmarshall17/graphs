#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint


class Edge:

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return str(self.src) + "->" + str(self.dst) + " weight: " + str(self.weight)


class Graph:

    def __init__(self, edge_list, node_cnt):
        self.edge_list = edge_list
        self.node_cnt = node_cnt

    def __str__(self):
        ret = ''
        for edge in self.edge_list:
            ret += str(edge) + '\n'
        return ret

    def BellmanFordShortestPath(self, source, end=None):

        # Initialize the distance from the source node S to all other nodes as
        # infinite and to itself as 0.
        distance = [float('inf')] * self.node_cnt
        distance[source] = 0
        parent = defaultdict(dict)

        for node in range(self.node_cnt):
            # If we don't modify the weights, then we're done so break out of the loop
            modified_weights = False
            for edge in self.edge_list:
                if (distance[edge.dst] > distance[edge.src] + edge.weight):
                    # print("Updating distance for %s from %s with weight %s" %
                    #       (
                    #           edge.dst,
                    #           edge.src,
                    #           edge.weight,
                    #       ))
                    distance[edge.dst] = distance[edge.src] + edge.weight
                    parent[edge.dst] = edge.src
                    modified_weights = True
            if not modified_weights:
                # if node < self.node_cnt - 1:
                #     print("Breaking out of loop early at %d instead of %d" %
                #           (
                #               node,
                #               self.node_cnt,
                #           ))
                break

        if end is not None:
            if end in parent:
                print(['%s: %s' % (k,parent[k]) for k in sorted(parent.keys()) ])
                shortest_path = [end]
                current = end
                while current != source:
                    shortest_path.append(parent[current])
                    current = parent[current]
                print("The shortest path from %s to %s is: %s" % (source,
                                                                  end,
                                                                  list(reversed(shortest_path))))
            else:
                raise ValueError("Invalid end node %s, no such node" % end)

        for edge in self.edge_list:

            if (distance[edge.dst] > distance[edge.src] + edge.weight):
                raise ValueError("Negative weight cycle exist in the graph")

        for node in range(self.node_cnt):
            print("Source Node(" + str(source) + ") -> Destination Node(" + str(node) + ") : " + str(distance[node]))




if __name__ == '__main__':
    e01 = Edge(0, 1, -1)
    e05 = Edge(0, 5, 2)
    e12 = Edge(1, 2, 2)
    e15 = Edge(1, 5, -2)
    e23 = Edge(2, 3, 5)
    e24 = Edge(2, 4, 1)
    e43 = Edge(4, 3, -4)
    e45 = Edge(4, 5, 3)
    e51 = Edge(5, 1, 2)
    e52 = Edge(5, 2, 3)

    edge_list = [e01, e05, e12, e15, e23, e24, e43, e45, e51, e52]
    node_cnt = 6
    source_node = 0

    g = Graph(edge_list, node_cnt)
    print("%s" % g)
    g.BellmanFordShortestPath(source_node, 4)
    g.BellmanFordShortestPath(source_node, 3)
    g.BellmanFordShortestPath(source_node, 2)
