import unittest
from BinaryTreeTraversals import BinaryTreeTraversals
from GraphClass import Vertex

class BinaryTreeTraversalTests(unittest.TestCase):

    def test_in_order(self):
        tree = [None, 10, 7, 11, 6, 8]
        visited = []
        btt = BinaryTreeTraversals()
        visited = btt.in_order(visited, tree, 10, len(tree) -1)
        correct_visted = [6, 7, 8, 10, 11]
        self.assertEqual(visited, correct_visted)

    def test_pre_order(self):
        tree = [None, 10, 7, 11, 6, 8]
        visited = []
        btt = BinaryTreeTraversals()
        visited = btt.pre_order(visited, tree, 10, len(tree) -1)
        correct_visted = [10, 7, 6, 8, 11]
        self.assertEqual(visited, correct_visted)

    def test_post_order(self):
        tree = [None, 10, 7, 11, 6, 8]
        visited = []
        btt = BinaryTreeTraversals()
        visited = btt.post_order(visited, tree, 10, len(tree) -1)
        correct_visted = [6, 8, 7, 11, 10]
        btt.post_order(visited, tree, 10, len(tree) -1)
        self.assertEqual(visited, correct_visted)
    # def test_max_path(self):
    #     a_vertex = Vertex('A', 10)
    #     b_vertex = Vertex('B', 7)
    #     c_vertex = Vertex('C', 11)
    #     d_vertex = Vertex('D', 6)
    #     e_vertex = Vertex('E', 8)
    #     tree = [None, a_vertex, b_vertex, c_vertex, d_vertex, e_vertex]
    #     btt = BinaryTreeTraversals()
    #     max_weight = 0
    #     actual_weight = btt.max_path(tree, max_weight, a_vertex)
    #     expect_weight = 15
    #     self.assertEqual(actual_weight, expect_weight)
