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

    def find_shortest_path(self, start, end):
        if self.weights:
            if self.negative_weights:
                return self.__bellman_ford__(start, end)
            return self.__dijkstra__(start, end)
        return self.__bfs__(start, end)

    def __bfs__(self, start, end):
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

    def __dijkstra__(self, start, end):
        print("__dijkstra__: start=%s end=%s" % (start, end))
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {start: (None, 0)}
        current_node = start
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.graph[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current_node
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

    def __bellman_ford__(self, start, end):
        # Initialize the distance from the source node S to all other nodes as
        # infinite and to itself as 0.
        node_count = len(self.graph.keys())
        distance = [float('inf')] * node_count
        distance[start] = 0
        parent = defaultdict(dict)

        for node in range(node_count):
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
