#!/usr/bin/env python3

from collections import defaultdict


# A Union Find class, aka Disjoint Set Union
class UnionFind:
    """
    UnionFind is a class the implements a union find, disjoint set union,
    with path compression and ranking in order to make it as efficient as
    possible. With both ranking and path compression, the time complexity
    is, according to Wikipedia, alpha(n) or "Inverse Ackermann" time. It
    also says that it may be O(log*n).
    The class is initialized with the number of expected elements.
    """
    def __init__(self, number):
        self.union_find = list(range(number))
        self.ranks = [0] * number

    @property
    def most_members(self):
        """
        This function will return the parent with the most members.
        """
        most_members = -1
        for parent in set(self.union_find):
            if most_members < 0:
                most_members = parent
            if self.union_find.count(parent) > self.union_find.count(most_members):
                most_members = parent
        return most_members

    def find(self, index):
        """
        Find the parent, i.e. the set to which this index belongs. We implement
        path compression here as well.
        :param index:
        :return: parent index
        """
        while index != self.union_find[index]:
            # print("find: %s" % self.union_find)
            self.union_find[index] = self.union_find[self.union_find[index]]
            index = self.union_find[index]
        return index

    def union(self, first, second):
        """
        Add the elements to the same set, i.e. parent. We use ranking to
        determine which element should become the parent.
        :param first: The first element
        :param second: The second element
        :return: None
        """
        first = self.find(first)
        second = self.find(second)
        if first == second:
            return

        if self.ranks[first] < self.ranks[second]:
            self.union_find[first] = self.union_find[second]
        elif self.ranks[first] > self.ranks[second]:
            self.union_find[second] = self.union_find[first]
        else:
            self.union_find[first] = self.union_find[second]
            self.ranks[second] += 1
