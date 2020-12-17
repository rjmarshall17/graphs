#!/usr/bin/env python3

# The min heap will contain the vertex ID followed by the current minimum cost to reach it
class DijkstraMinHeap:
    def __init__(self, array):
        self.vertex_map = {index:index for index in range(len(array))}
        self.heap = self.__build_heap__(array)

    def is_empty(self):
        return len(self.heap) == 0

    def __build_heap__(self, array):
        first_parent = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent + 1)):
            self.__sift_down__(current_index, len(array) - 1, array)
        return array

    # O(log(n)) time, O(1) space
    def __sift_down__(self, current_index, end_index, heap):
        first_child_index = current_index * 2 + 1
        while first_child_index < end_index:
            second_child_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1
            if second_child_index != -1 and heap[second_child_index][1] < heap[first_child_index][1]:
                index_to_swap = second_child_index
            else:
                index_to_swap = first_child_index
            if heap[index_to_swap][1] < heap[current_index][1]:
                self.__swap__(current_index, index_to_swap, heap)
                current_index = index_to_swap
                first_child_index = current_index * 2 + 1
            else:
                return

    # O(log(n)) time, O(1) space
    def __sift_up__(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index][1] < heap[parent_index][1]:
            self.__swap__(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    # O(log(n)) time, O(1) space
    def pop(self):
        if self.is_empty():
            return
        self.__swap__(0, len(self.heap) - 1, self.heap)
        vertex, cost = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.__sift_down__(0, len(self.heap) -1, self.heap)
        return vertex, cost

    def __swap__(self, first_index, second_index, heap):
        self.vertex_map[heap[first_index][0]] = second_index
        self.vertex_map[heap[second_index][0]] = first_index
        heap[first_index], heap[second_index] = heap[second_index], heap[first_index]

    def update(self, vertex, value):
        self.heap[self.vertex_map[vertex]] = (vertex, value)
        self.__sift_up__(self.vertex_map[vertex], self.heap)


def dijkstra_algorithm(start, edges):
    number_of_nodes = len(edges)

    minimum_costs = [float('inf') for _ in range(number_of_nodes)]
    minimum_costs[start] = 0

    minimum_costs_heap = DijkstraMinHeap([(index, float('inf')) for index in range(number_of_nodes)])
    minimum_costs_heap.update(start, 0)

    while not minimum_costs_heap.is_empty():
        vertex, current_cost = minimum_costs_heap.pop()
        # If the cost for this particular vertex has not been changed, then it's not reachable
        if current_cost == float('inf'):
            break
        for destination, cost in edges[vertex]:
            new_cost = current_cost + int(cost)
            current_destination_cost = minimum_costs[destination]
            if new_cost < current_destination_cost:
                minimum_costs[destination] = new_cost
                minimum_costs_heap.update(destination, new_cost)

    return list(map(lambda x: -1 if x == float('inf') else x, minimum_costs))


EXAMPLE_INPUTS = [
    {
        'start': 0,
        "edges": [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []],
     },
    {
        "start": 1,
        "edges": [[], [], [], []],
    },
    {
        "edges": [
            [[1, 1], [3, 1]],
            [[2, 1]],
            [[6, 1]],
            [[1, 3], [2, 4], [4, 2], [5, 3], [6, 5]],
            [[5, 1]],
            [[4, 1]],
            [[5, 2]],
            [[0, 7]]
        ],
        "start": 7
    },
    {
        "edges": [
            [[1, 3], [2, 2]],
            [[3, 7]],
            [[1, 2], [3, 4], [4, 1]],
            [],
            [[0, 2], [1, 8], [3, 1]]
        ],
        "start": 4,
    },
]

EXPECTED_RESULTS = [
    [0, 7, 13, 27, 10, -1],
    [-1, 0, -1, -1],
    [7, 8, 9, 8, 10, 11, 10, 0],
    [2, 5, 4, 1, 0],
]


if __name__ == '__main__':
    for input_index, input_data in enumerate(EXAMPLE_INPUTS):
        for i, edges in enumerate(input_data['edges']):
            print("The edges/costs for %d are: %s" % (i, edges))
        result = dijkstra_algorithm(input_data['start'], input_data['edges'])
        print("The result for start %d is: %s" % (input_data['start'],
                                                  ' '.join(["%d - %s" % (i, x) for i,x in enumerate(result)])))
        assert result == EXPECTED_RESULTS[input_index], \
            "The result did not match the expected: %s" %  EXPECTED_RESULTS[input_index]
