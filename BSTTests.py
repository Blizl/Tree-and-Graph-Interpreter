import unittest
from BST import BST, Node


class BSTTests(unittest.TestCase):
    def testInsert(self):
        node_1 = Node(4,  None, None)
        bst = BST()
        bst.insert(node_1, 3)
        self.assertEquals(node_1.left.data, 3)

    def testInsertTwoNodes(self):
        node_1 = Node(5,None,None)
        bst = BST()
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        self.assertEquals(node_1.left.left.data,2)

    def testInsertThreeNodes(self):
        node_1 = Node(5,None,None)
        bst = BST()
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        bst.insert(node_1, 1)
        self.assertEquals(node_1.left.left.left.data, 1)

    def testInsertFourNodes(self):
        node_1 = Node(5,None,None)
        bst = BST()
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        bst.insert(node_1, 1)
        bst.insert(node_1, 6)
        self.assertEquals(node_1.right.data, 6)

    def testRemoveLeafNode(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST()
        bst.removeNode(None, node_5, 6)
        self.assertEquals(node_5.right, None)

    def testRemoveLeafNode2(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST()
        bst.removeNode(None, node_5, 1)
        self.assertEquals(node_2.left, None)

    def testRemoveNodeHasOneChildren(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST()
        bst.removeNode(None, node_5, 2)
        self.assertEquals(node_3.left.data, 1)

    def testRemoveNodeHasTwoChildrenLeftSubTree(self):
        node_1 = Node(1, None, None)
        node_6 = Node(3, None, None)
        node_2 = Node(2, node_1, node_6)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST()
        bst.removeNode(None, node_5, 2)
        self.assertEquals(node_3.left.data, 3)
        self.assertEqual(node_3.left.left.data, 1)

    def testRemoveNodeHasTwoChildrenRightSubtree(self):
        node_1 = Node(1, None, None)
        node_6 = Node(3, None, None)
        node_2 = Node(2, node_1, node_6)
        node_0 = Node(0, None, None)
        node_8 = Node(8, None, None)
        node_7 = Node(7, node_0, node_8)
        node_3 = Node(4, node_2, node_7)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST()
        bst.removeNode(None, node_5, 7)
        self.assertEquals(node_3.right.data, 8)
    def testOr(self):
        self.assertFalse(True ^ True);