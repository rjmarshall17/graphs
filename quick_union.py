#!/usr/bin/env python3

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
