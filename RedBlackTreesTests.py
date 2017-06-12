import unittest
from RedBlackTrees import RedBlackNode, RedBlackTree


class RedBlackTreeTests(unittest.TestCase):
    def test_is_red_positive(self):
        red_node = RedBlackNode(5, None, None, "red")
        self.assertTrue(red_node.is_red())

    def test_is_red_negative(self):
        node = RedBlackNode(5, None, None, "black")
        self.assertFalse(node.is_red())

    def test_is_black_positive(self):
        black_node = RedBlackNode(5, None, None, "black")
        self.assertTrue(black_node.is_black())

    def test_is_black_negative(self):
        node = RedBlackNode(5, None, None, "red")
        self.assertFalse(node.is_black())

    def test_insert_method(self):
        root_node = RedBlackNode(1, None, None, "black", True)
        node_4 = RedBlackNode(4, None, None, "red")
        rb_tree = RedBlackTree(root_node)
        rb_tree.insert(rb_tree.root, node_4)
        self.assertEquals(rb_tree.root.right.data, 4)
        self.assertTrue(rb_tree.root.is_black())
        self.assertTrue(rb_tree.root.right.is_red())

    def test_complicated_rb_tree(self):
        root_node = RedBlackNode(11, None, None, "black", True)
        rb_tree = RedBlackTree(root_node)
        node_2 = RedBlackNode(2, None, None, "red")
        node_1 = RedBlackNode(1, None, None, "red")
        node_14 = RedBlackNode(14, None, None, "red")
        node_15 = RedBlackNode(15, None, None, "red")
        node_7 = RedBlackNode(7, None, None, "red")
        node_5 = RedBlackNode(5, None, None, "red")
        node_4 = RedBlackNode(4, None, None, "red")
        rb_tree.insert(rb_tree.root, node_2)
        rb_tree.insert(rb_tree.root, node_1)
        rb_tree.insert(rb_tree.root, node_14)
        rb_tree.insert(rb_tree.root, node_15)
        rb_tree.insert(rb_tree.root, node_7)
        rb_tree.insert(rb_tree.root, node_5)
        rb_tree.insert(rb_tree.root, node_4)
        self.assertTrue(rb_tree.maintains_rb_properties())

    def test_all_red_nodes_have_black_children_negative(self):
        # Note this breaks red black tree property of root node being black
        red_node2 = RedBlackNode(2, None, None, "red")
        red_node = RedBlackNode(1, None, red_node2, "red", True)
        rb_tree = RedBlackTree(red_node)
        self.assertFalse(rb_tree.all_red_nodes_have_black_children(rb_tree.root))

    def test_remove(self):
        root_node = RedBlackNode(1, None, None, "black", True)
        node_2 = RedBlackNode(2, None, None, "red")
        rb_tree = RedBlackTree(root_node)
        rb_tree.insert(rb_tree.root, node_2)
        rb_tree.remove(node_2)
        self.assertFalse(rb_tree.search(rb_tree.root, 2))

    def test_complicated_remove(self):
        root_node = RedBlackNode(11, None, None, "black", True)
        rb_tree = RedBlackTree(root_node)
        node_2 = RedBlackNode(2, None, None, "red")
        node_1 = RedBlackNode(1, None, None, "red")
        node_14 = RedBlackNode(14, None, None, "red")
        node_15 = RedBlackNode(15, None, None, "red")
        node_7 = RedBlackNode(7, None, None, "red")
        node_5 = RedBlackNode(5, None, None, "red")
        node_4 = RedBlackNode(4, None, None, "red")
        rb_tree.insert(rb_tree.root, node_2)
        rb_tree.insert(rb_tree.root, node_1)
        rb_tree.insert(rb_tree.root, node_14)
        rb_tree.insert(rb_tree.root, node_15)
        rb_tree.insert(rb_tree.root, node_7)
        rb_tree.insert(rb_tree.root, node_5)
        rb_tree.insert(rb_tree.root, node_4)
        rb_tree.remove(node_2)
        self.assertFalse(rb_tree.search(rb_tree.root, 2))
        self.assertTrue(rb_tree.maintains_rb_properties())

    def test_get_black_height(self):
        root_node = RedBlackNode(5, None, None, "black", True)
        rb_tree = RedBlackTree(root_node)
        node_8 = RedBlackNode(8, None, None, "red")
        node_7 = RedBlackNode(7, None, None, "red")
        node_4 = RedBlackNode(4, None, None, "red")
        self.assertEquals(rb_tree.get_black_height(rb_tree.root), 2)
