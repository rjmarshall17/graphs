#!/usr/bin/env python3

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