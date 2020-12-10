#!/usr/bin/env python3

from typing import List
graph = {
    "A":{}
}


class UnionFind:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


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
