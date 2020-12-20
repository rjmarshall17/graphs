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


graph = {
    "A": {}
}


class DSU(object):
    def __init__(self, size):
        if isinstance(size, int):
            if size <= 0:
                raise ValueError("Invalid size, must be greater than 0")
        else:
            raise ValueError("Invalid size, must be an integer")
        self.par = [x for x in range(size)]
        self.rnk = [0] * size

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class QuickFind:
    def __init__(self, size: int):
        self.id = [-1] * size
        for i in range(size):
            self.id[i] = i

    def __str__(self):
        return ",".join(map(str, self.id))

    def __check_vertices__(self, v1, v2):
        if v1 < 0 or v2 < 0:
            raise ValueError('Vertices must be positive integers')
        if v1 >= len(self.id):
            raise ValueError("Invalid vertex number 1, too large")
        if v2 >= len(self.id):
            raise ValueError("Invalid vertex number 2, too large")

    def find(self, vertex1: int, vertex2: int):
        self.__check_vertices__(vertex1, vertex2)
        return self.id[vertex1] == self.id[vertex2]

    def unite(self, vertex1: int, vertex2: int):
        parent_id = self.id[vertex1]
        for i in range(len(self.id)):
            if self.id[i] == parent_id:
                self.id[i] = self.id[vertex2]


class QuickUnion:
    def __init__(self, size: int):
        self.id = [-1] * size
        for i in range(size):
            self.id[i] = i

    def __str__(self):
        return ",".join(map(str, self.id))

    def __check_indexes__(self, p: int, q: int):
        if p < 0 or q < 0:
            raise ValueError('Vertices must be positive integers')
        if p >= len(self.id):
            raise ValueError("Invalid index p, too large")
        if q >= len(self.id):
            raise ValueError("Invalid index q, too large")

    def root(self, i: int):
        if i < 0 or i >= len(self.id):
            raise ValueError("Invalid index i: %d" % i)
        while i != self.id[i]:
            i = self.id[i]

    def find(self, p: int, q: int):
        self.__check_indexes__(p, q)
        return self.id[p] == self.id[q]

    def unite(self, p: int, q: int):
        self.__check_indexes__(p, q)
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j
