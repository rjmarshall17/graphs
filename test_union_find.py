#!/usr/bin/env python3

import unittest
from union_find import UnionFind

class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(10)

    def test_create(self):
        self.assertEqual(len(self.uf.union_find),
                         10,
                         "The size of the union find should be 10")

    def test_initial_contents(self):
        self.assertEqual(self.uf.union_find,
                         [0,1,2,3,4,5,6,7,8,9],
                         "The initial content should be a list from 0 to 9")

    def test_union_1_2_3(self):
        self.uf.union(1,3)
        self.uf.union(2,3)
        self.assertEqual(self.uf.union_find,
                         [0,3,3,3,4,5,6,7,8,9],
                         "The parent of 1 and 2 should be 3: %s" % self.uf.union_find)

    def test_most_members(self):
        self.uf.union(3,4)
        self.uf.union(5,4)
        self.uf.union(6,4)
        print("The most members returns: %s" % self.uf.most_members)
        self.assertEqual(self.uf.most_members,
                         [(4,4)],
                         "The parent with the most members should be 4: %s" %
                         self.uf.union_find)


if __name__ == '__main__':
    unittest.main()