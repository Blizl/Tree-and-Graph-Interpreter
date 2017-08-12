import unittest
from AVLTree import AVLNode, AVLTree


class AVLTreeTests(unittest.TestCase):
    """TODO: Need to add test for printing out nodes"""
    def testAVLNode(self):
        avl_node = AVLNode(9, None, None)
        self.assertEquals(0, avl_node.balance_factor)
        avl_node.balance_factor = 10
        self.assertEquals(10, avl_node.balance_factor)

    def testAVLTreeInherited(self):
        avl_node = AVLNode(5, None, None)
        avl_tree = AVLTree(avl_node)
        avl_tree.insert(avl_node, 6)
        self.assertTrue(avl_tree.search(avl_node, 6))
        self.assertEquals(1, avl_tree.get_height(avl_node))

    def testRightRotation(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 2)
        self.assertEquals(avl_tree.root.data, 4)
        self.assertEquals(avl_tree.root.left.data, 2)
        self.assertEquals(avl_tree.root.right.data, 5)

    def testRightRotationv2(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 2)
        avl_tree.insert(avl_tree.root, 6)
        self.assertEquals(avl_tree.root.left.data, 2)

    def testLeftRotation(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(root_node, 6)
        avl_tree.insert(root_node, 7)
        self.assertEquals(avl_tree.root.data, 6)
        self.assertEquals(avl_tree.root.left.data, 5)
        self.assertEquals(avl_tree.root.right.data, 7)
        self.assertEquals(avl_tree.root.left.parent, avl_tree.root)
        self.assertEquals(avl_tree.root.right.parent, avl_tree.root)
        self.assertEquals(avl_tree.root.parent, None)

    def testParentNode(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 2)
        avl_tree.insert(avl_tree.root, 6)
        self.assertEquals(avl_tree.root.left.parent, avl_tree.root)

    def testIsLeftChild(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 2)
        avl_tree.insert(avl_tree.root, 6)
        self.assertTrue(avl_tree.root.left.is_left_child())

    def testisRightChild(self):
        root_node = AVLNode(5, None, None)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(root_node, 4)
        avl_tree.insert(root_node, 2)
        avl_tree.insert(root_node, 6)
        self.assertTrue(root_node.right.is_right_child())

    def testLeftRightRotate(self):
        root_node = AVLNode(4, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(root_node, 2)
        avl_tree.insert(root_node, 3)
        self.assertEquals(avl_tree.root.data, 3)
        self.assertEquals(avl_tree.root.left.data, 2)
        self.assertEquals(avl_tree.root.right.data, 4)

    def testRightLeftRotate(self):
        root_node = AVLNode(4, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(root_node, 6)
        avl_tree.insert(root_node, 5)
        self.assertEquals(avl_tree.root.data, 5)
        self.assertEquals(avl_tree.root.left.data, 4)
        self.assertEquals(avl_tree.root.right.data, 6)

    """New algorithm approach, following the book"""
    def testBalancedAVLTree(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 6)
        avl_tree.insert(avl_tree.root, 7)
        avl_tree.insert(avl_tree.root, 8)
        avl_tree.insert(avl_tree.root, 1)

    def testLeftRotateRoot(self):
        root_node=  AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 6)
        avl_tree.insert(avl_tree.root, 7)


    def testLeftRotateNonRoot(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 6)
        avl_tree.insert(avl_tree.root, 7)
        avl_tree.insert(avl_tree.root, 8)
        self.assertTrue(avl_tree.allNodesRightAreLarger())
        self.assertTrue(avl_tree.nodes_left_are_smaller())

    def testIsRightChild(self):
        root_node = AVLNode(5, None, None)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 6)
        self.assertTrue(root_node.right.is_right_child())

    def testRightRotateRoot(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 3)
        self.assertTrue(avl_tree.allNodesRightAreLarger())
        self.assertTrue(avl_tree.nodes_left_are_smaller())

    def testRightRotateNonRoot(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 3)
        avl_tree.insert(avl_tree.root, 1)
        self.assertTrue(avl_tree.allNodesRightAreLarger())
        self.assertTrue(avl_tree.nodes_left_are_smaller())

    def testAllNodesRightAreLargerPositive(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 3)
        self.assertTrue(avl_tree.allNodesRightAreLarger())

    def testAllNodesRightAreLargerNegative(self):
        node_1 = AVLNode(1, None, None)
        root_node = AVLNode(5, None, node_1, True)
        avl_tree = AVLTree(root_node)
        self.assertFalse(avl_tree.allNodesRightAreLarger())

    def testallNodesLeftAreSmallerPositive(self):
        root_node = AVLNode(5, None, None)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 3)
        avl_tree.insert(avl_tree.root, 2)
        self.assertTrue(avl_tree.nodes_left_are_smaller())

    def testallNodesLeftAreSmallerNegative(self):
        node_1 = AVLNode(7, None, None)
        root_node = AVLNode(5, node_1, None)
        avl_tree = AVLTree(root_node)
        self.assertFalse(avl_tree.nodes_left_are_smaller())

    def testrightRotateTestV3(self):
        root_node = AVLNode(5, None, None, True)
        avl_tree = AVLTree(root_node)
        avl_tree.insert(avl_tree.root, 4)
        avl_tree.insert(avl_tree.root, 3)
        avl_tree.insert(avl_tree.root, 2)
        avl_tree.insert(avl_tree.root, 1)
        avl_tree.insert(avl_tree.root, 6)
        avl_tree.printAllNodes()
        self.assertTrue(avl_tree.allNodesRightAreLarger())
        self.assertTrue(avl_tree.nodes_left_are_smaller())
        self.assertEquals(avl_tree.root.left.data, 2)
        self.assertEquals(avl_tree.root.left.left.data, 1)
        self.assertEquals(avl_tree.root.left.right.data, 3)
        self.assertEquals(avl_tree.root.right.data, 5)
        self.assertEquals(avl_tree.root.right.right.data, 6)
