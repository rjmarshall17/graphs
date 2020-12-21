#!/usr/bin/env python3

from collections import defaultdict

# A Union Find class, aka Disjoint Set Union
class UnionFind:
    """
    UnionFind is a class the implements a union find, disjoint set union,
    with path compression and ranking in order to make it as efficient as
    possible. With both ranking and path compression, the time complexity
    is, according to Wikipedia, alph(n) or "Inverse Ackermann" time. It
    also says that it may be O(log*n).
    The class is initialized with the number of expected elements.
    """
    def __init__(self, number):
        self.union_find = list(range(number))
        self.ranks = [0] * number

    @property
    def most_members(self):
        """
        This function determines the parent(s) with the most members for
        each of the parents. It returns a list of tuples where the first
        element is the parent ID and the second element is the number of
        members for that parent.
        most_members -> [(p,n),...] where p=parent and n=number of elements
        for that parent.
        """
        ret = defaultdict(list)
        # At each index of the union find should be the parent ID,
        # i.e. the index of the parent, so build list of the indices
        # with the same parent.
        members = [(-1,0)]
        for i, parent in enumerate(self.union_find):
            ret[parent].append(i)
            if len(ret[parent]) > members[0][1]:
                members = [(parent, len(ret[parent]))]
            elif len(ret[parent]) == members[0][1]:
                members.append((parent, len(ret[parent])))

        return members

    def find(self, index):
        """
        Find the parent, i.e. the set to which this index belongs. We implement
        path compression here as well.
        :param index:
        :return: parent index
        """
        while index != self.union_find[index]:
            print("find: %s" % self.union_find)
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
