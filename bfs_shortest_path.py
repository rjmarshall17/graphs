#!/usr/bin/env python3
from collections import defaultdict, deque

# Python implementation to find the
# shortest path in the graph using
# defaultdict


# Function to find the shortest path between two
# nodes of an undirected graph, make sure that the
# nodes are setup with neighbors in both directions
# i.e. if there is a connection from 1->2 then there
# also needs to be a connection from 2->1.
def BreadthFirstSearchShortestPath(graph, start, end):
    visited = []

    # Queue for traversing the graph in the BFS. Use a 
    # deque since this is a queue and a deque popleft()
    # has a time complexity of O(1) vs. O(n-k), where 
    # n=length of the list and k is the index being 
    # popped, for a normal list.
    queue = deque()
    queue.append([start])

    # If the desired node is
    # reached
    if start == end:
        return [start]

    # Loop to traverse the graph with the help of the queue
    while queue:
        bfs_path = queue.popleft()
        node = bfs_path[-1]
        # print("node=%s" % node)

        # Condition to check if the current node is not visited
        if node not in visited:
            neighbors = graph[node]
            # print("Neighbors for %s: %s" % (node,neighbors))

            # Loop to iterate over the
            # neighbours of the node
            for neighbor in neighbors:
                new_path = list(bfs_path)
                new_path.append(neighbor)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the end
                if neighbor == end:
                    return new_path
            visited.append(node)

            # Condition when the nodes
    # are not connected
    return []


# For an undirected graph we need to make sure that we show connections
# in both directions
EDGES_FOR_TEST2 = [
    (1, 2),
    (2, 4),
    (2, 5),
    (1, 6),
    (6, 9),
    (6, 10),
    (1, 3),
    (3, 7),
    (3, 8),
]

BANK_TRANSFER_DATA = [
    (4, 2, 2),
    (5, 1, 2),
    (2, 4, 1),
    (9, 10, 5),
    (7, 10, 100),
    (1, 5, 8),
    (9, 10, 2),
    (7, 10, 3),
]

FROM_BANK = 0
TO_BANK = 1
THRESHOLD = 2

# Driver Code
if __name__ == "__main__":
    # Graph using dictionaries
    graph = {'A': ['B', 'E', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B', 'E'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}

    # Function Call
    print(BreadthFirstSearchShortestPath(graph, 'D', 'A'))

    graph2 = defaultdict(list)
    # The graph needs to be an undirected graph for the above
    # BFS to work, so be sure to add edges for both directions
    for edge in EDGES_FOR_TEST2:
        graph2[edge[0]].append(edge[1])
        graph2[edge[1]].append(edge[0])

    print(graph2)
    print("Shortest path for 4->2: %s" % BreadthFirstSearchShortestPath(graph2,4,2))
    print("Shortest path for 10->2: %s" % BreadthFirstSearchShortestPath(graph2,10,2))
    print("Shortest path for 5->1: %s" % BreadthFirstSearchShortestPath(graph2,5,1))
    print("Shortest path for 6->9: %s" % BreadthFirstSearchShortestPath(graph2,6,9))

    print("Checking bank transfers:")
    transfer_succeeds = False
    for transfer in BANK_TRANSFER_DATA:
        # print("from=%s to=%s threshold=%s" % (transfer[FROM_BANK],transfer[TO_BANK],transfer[THRESHOLD]))
        path = BreadthFirstSearchShortestPath(graph2,transfer[FROM_BANK],transfer[TO_BANK])
        if len(path) <= transfer[THRESHOLD]:
            transfer_succeeds = True
        else:
            transfer_succeeds = False
        print("For transfer from %2d to %2d with threshold %3d succeeds: %3s using path: %s" %
              (transfer[FROM_BANK],
               transfer[TO_BANK],
               transfer[THRESHOLD],
               "YES" if transfer_succeeds else "NO",
               path
               ))
