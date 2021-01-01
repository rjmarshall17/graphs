#!/usr/bin/env python3

from collections import defaultdict, deque


class Graph:
    def __init__(self, graph_data=None, weights=None):
        self.graph = defaultdict(list)
        self.weights = {}
        self.negative_weights = False

        # If the incoming graph data is a dictionary, assume that it is
        # already in an acceptable format, i.e. a dictionary where the
        # keys are the vertices and the values are a list of neighbors.
        # If we also get a list of weights, the format is: (src,dst),cost
        if isinstance(graph_data, dict):
            for k,v in graph_data.items():
                if not isinstance(v, list):
                    raise ValueError("The graph data must have a list for edges")
            self.graph = graph_data
        if weights is not None:
            for src_dst, cost in weights:
                self.weights[src_dst] = cost
                if cost < 0:
                    self.negative_weights = True

    def add_edge(self, source, destination, cost=None):
        """
        Add destination to the list of edges for source
        :param source:
        :param destination:
        :param cost: If None, no cost
        :return:
        """
        self.graph[source].append(destination)
        # If we are using weights, then ensure that every edge has at least a cost of 1
        if cost is None:
            if self.weights:
                self.weights[(source, destination)] = 1
        else:
            self.weights[(source, destination)] = cost
            if cost < 0:
                self.negative_weights = True

    def find_path(self, start, end):
        """
        Find path is synonymous with find shortest path.
        :param start:
        :param end:
        :return:
        """
        return self.find_shortest_path(start, end)

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_shortest_path(self, start, end=None):
        if self.weights:
            if self.negative_weights:
                return self.__bellman_ford__(start, end)
            return self.__dijkstra__(start, end)
        return self.__bfs__(start, end)

    def __bfs__(self, start, end=None):
        """
        Use a breadth first search to determine the shortest path
        in linear time, i.e. O(n).
        :param start:
        :param end:
        :param path:
        :return:
        """
        if start == end:
            return [start]

        visited = []
        queue = deque()
        queue.append([start])
        while queue:
            current_path = queue.popleft()
            current_node = current_path[-1]
            if current_node not in visited:
                neighbors = self.graph[current_node]

                # Loop to iterate over the neighbours of the node. For each new neighbor
                # add them to the current_path, the path we popped from the queue,
                # so that the nodes can be checked if they have not already been visited.
                for neighbor in neighbors:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    # Condition to check if the neighbour node is the end
                    if neighbor == end:
                        return new_path
                    queue.append(new_path)
                visited.append(current_node)

        # Condition when the nodes are not connected
        return []

    def __dijkstra__(self, start, end=None):
        queue = deque()
        distances = {}
        parents = {}

        # We want the start to be at the head of the queue because it will be the vertex with the lowest
        # distance to start.
        queue.append(start)
        for vertex in self.graph.keys():
            distances[vertex] = float('inf')
            parents[vertex] = None
            if vertex not in queue:
                queue.append(vertex)

        distances[start] = 0

        while len(queue) > 0:
            vertex = queue.popleft()
            if end is not None:
                if vertex == end:
                    break
            for edge in self.graph[vertex]:
                if distances[edge] > distances[vertex] + self.weights[(vertex, edge)]:
                    distances[edge] = distances[vertex] + self.weights[(vertex, edge)]
                    parents[edge] = vertex

        if end is not None:
            if end in parents:
                return_deque = deque()
                current = end
                while True:
                    if current is None:
                        return []
                    return_deque.appendleft(current)
                    if current == start:
                        break
                    current = parents[current]
                return list(return_deque)
            else:
                raise ValueError("Invalid end node: %s" % end)
        return distances, parents

    def __bellman_ford__(self, start, end=None):
        distances = {}
        parents = {}

        for vertex in self.graph.keys():
            distances[vertex] = float('inf')
            parents[vertex] = None

        distances[start] = 0

        for i in range(len(self.graph) - 1):
            # print("Iteration %d" % i)
            distances_modified = False
            for src_dst, weight in self.weights.items():
                if distances[src_dst[0]] + weight < distances[src_dst[1]]:
                    distances[src_dst[1]] = distances[src_dst[0]] + weight
                    parents[src_dst[1]] = src_dst[0]
                    distances_modified = True
            if not distances_modified:
                # print("Breaking out at iteration: %d" % i)
                break

        for src_dst, weight in self.weights.items():
            if distances[src_dst[0]] + weight < distances[src_dst[1]]:
                raise ValueError('The graph has a negative cycle')

        if end is not None:
            if end in parents:
                if parents[end] is None:
                    raise ValueError('No path to node %s' % end)
                # print(['%s: %s' % (k,parent[k]) for k in sorted(parent.keys()) ])
                shortest_path = [end]
                current = end
                while current != start:
                    shortest_path.append(parents[current])
                    current = parents[current]
                # print("The shortest path from %s to %s is: %s" % (start,
                #                                                   end,
                #                                                   shortest_path[::-1]))
                return shortest_path[::-1]
            else:
                raise ValueError("Invalid end node %s, no such node" % end)

        return distances, parents

    def depth_first_search(self, start):
        stack = [start]
        array = []
        while len(stack) > 0:
            # print("Current stack: %s" % stack)
            current = stack.pop()
            # print("Popped: %s" % s)
            # If current is not in the graph, i.e. not a key/parent only a child, add it to the array
            if current not in self.graph:
                # print("current (%s) was not in the graph %s" % (current, self.graph))
                array.append(current)
            if current not in array:
                array.append(current)
                # current is a key in the graph, and has neighbors/children
                for node in self.graph[current]:
                    stack.append(node)
                    # print('Appended to stack: %s' % node)
        # 		else:
        # 			print("%s was in array" % current)
        return array
