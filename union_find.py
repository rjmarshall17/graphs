#!/usr/bin/env python3
from typing import List


# A Union Find class, aka Disjoint Set Union
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, s):
        if s in self.parent:
            return
        self.parent[s] = s
        self.size[s] = 1

    def find(self, s):
        p = self.parent[s]
        while self.parent[p] != p:
            p = self.parent[p]

        while s != p:
            s, self.parent[s] = self.parent[s], p

        return p

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.size[a] > self.size[b]:
            a, b = b, a

        self.parent[a] = b
        self.size[b] += self.size[a]


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
