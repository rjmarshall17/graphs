#!/usr/bin/env python3

from typing import List

"""
Single Cycle Check

You're given an array of integers where each integer represents a jump of its value in the array. For
instance, the integer 2 represents a jump of two indices forward in the array; the integer -3 represents
a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance a jump of -1 at
index 0 brings us to the last index of the array. Similarly, a jump of 1 at the last index in the array
brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a cycle. A single
cycle occurs if, starting at any index in the array and following the jumps, every element in the array is
visited exactly once before landing back at the starting index.
"""

EXAMPLE_INPUTS = [
    [2, 3, 1, -4, -4, 2],
    [2, 2, -1],
    [2, 2, 2],
    [1, 1, 1, 1, 1],
]

EXPECTED_RESULTS = [
    True,
    True,
    True,
    True,
]


def hasSingleCycle(array: List[int]) -> bool:
    num_elements_visited = 0
    current_index = 0
    index_array = []
    while num_elements_visited < len(array):
        index_array.append(current_index)
        if num_elements_visited > 0 and current_index == 0:
            return False
        num_elements_visited += 1
        current_index = getNextIdx(current_index, array)
    return current_index == 0


def getNextIdx(current_idx: int, array: List[int]) -> int:
    next_idx = (current_idx + array[current_idx]) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = hasSingleCycle(input_data)
        assert result == EXPECTED_RESULTS[i],\
            "The result, %s, does not match the expected result: %s" % (result,
                                                                        EXPECTED_RESULTS[i])
        print("The results for %s: %s match the expected result: %s" % (input_data, result, EXPECTED_RESULTS[i]))
