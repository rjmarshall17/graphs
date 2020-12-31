#!/usr/bin/env python3

from collections import defaultdict
from random import randint


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def __str__(self):
        ret = str(self.edges)
        ret += '\n'
        ret += str(self.weights)
        return ret

    def add_edge(self, source, destination, cost=1):
        self.edges[source].append(destination)
        self.weights[(source, destination)] = cost


def dijkstra(dijkstra_graph, dijkstra_start, dijkstra_end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {dijkstra_start: (None, 0)}
    current_node = dijkstra_start
    visited = set()

    while current_node != dijkstra_end:
        visited.add(current_node)
        destinations = dijkstra_graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = dijkstra_graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


# For these examples we are using undirected graphs. If there is an edge from 1->2 then
# there must also be an edge from 2->1
EXAMPLE_INPUT = [
    [
        (1, 2),
        (2, 1),
        (2, 4),
        (4, 2),
        (2, 5),
        (5, 2),
        (1, 6),
        (6, 1),
        (6, 9),
        (9, 6),
        (6, 10),
        (10, 6),
        (1, 3),
        (3, 1),
        (3, 7),
        (7, 3),
        (3, 8),
        (8, 3),
    ],
]


if __name__ == '__main__':
    for input_index, input_data in enumerate(EXAMPLE_INPUT):
        graph = Graph()
        for edge in input_data:
            if len(edge) == 3:
                graph.add_edge(edge[0], edge[1], edge[2])
            else:
                graph.add_edge(edge[0], edge[1])
        print('%s' % graph)
        for i in range(10):
            start, end = randint(1,10), randint(1,10)
            result = dijkstra(graph, start, end)
            print("Result for %d to %d was: %s" % (start, end, result))