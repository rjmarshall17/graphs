#!/usr/bin/env python3

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