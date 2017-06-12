#pylint: disable=C0111
#pylint: disable=R0201


class Node(object):
    def __init__(self, data, left, right, is_root=False, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.is_root = is_root
        self.parent = parent

    def __repr__(self):
        return "Node data is %s" %(self.data)

    def has_left_child(self):
        if self.left is not None:
            return True
        else:
            return False

    def has_right_child(self):
        if self.right is not None:
            return True
        else:
            return False

    def has_no_children(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def is_left_child(self):
        if self.parent is not None:
            if self.parent.left is not None and self.parent.left.data == self.data:
                return True
            else:
                return False

    def is_right_child(self):
        if self.parent is not None:
            if self.parent.right is not None and self.parent.right.data == self.data:
                return True
            else:
                return False

class BST(object):
    """TODO: Refactor methods so that functions are based off of root instead of taking in a node"""
    def __init__(self, root):
        self.root = root

    def insert(self, node, value):
        if node is None:
            node = Node(value, None, None, False, None)
        else:
            if node.data > value:
                if node.left is None:
                    node.left = Node(value, None, None, False, node)
                else:
                    self.insert(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value, None, None, False, node)
                else:
                    self.insert(node.right, value)

    def search(self, node, value):
        # if node is None or node.data == value:
        #     return node
        if node is None:
            return False
        if node.data == value:
            return True

        if node.data > value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def removeNode(self, prev_node, curr_node, value):
        if curr_node.data == value:

            if self.no_child(curr_node):
                if prev_node.data > curr_node.data:
                    prev_node.left = None
                else:
                    prev_node.right = None
            elif self.one_child(curr_node):
                if prev_node.data > curr_node.data:
                    prev_node.left = curr_node.left
                else:
                    prev_node.right = curr_node.right
            else:
                if prev_node.data > curr_node.data:
                    # Find the largest node in the right subtree to replace current node
                    prev_node.left = self.get_min_node(curr_node)
                    # Set the right and left of current node to the replacement node
                    prev_node.left.left = curr_node.left
                    prev_node.left.right = curr_node.right
                else:
                    prev_node.right = self.get_min_node(curr_node)
                    prev_node.right.left = curr_node.left
                    prev_node.right.right = curr_node.right
            curr_node = None
            return

        if curr_node.data > value:
            self.removeNode(curr_node, curr_node.left, value)
        else:
            self.removeNode(curr_node, curr_node.right, value)

    def get_min_node(self, curr_node):
        return self.get_min_node_helper(curr_node.right, curr_node.right)

    def get_min_node_helper(self, node, min):
        if node is None:
            return
        if node.left and node.left.data < min.data:
            min = node.left
        if node.right and node.right.data < min.data:
            min = node.right
        self.get_min_node_helper(node.left, min)
        self.get_min_node_helper(node.right, min)
        return min

    def no_child(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def one_child(self, node):
        if self.xor(node.left, node.right):
            return True
        else:
            return False

    def get_height(self, node):
        if node is None:
            return
        if node.left:
            return 1 + self.get_height(node.left)
        if node.right:
            return 1 + self.get_height(node.right)
        return 0

    def xor(self, node1, node2):
        if node1 is None and node2 is None:
            return False
        if node1 is not None and node2 is not None:
            return False
        return True

    def printAllNodes(self):
        self.printNode(self.root)

    def printNode(self, node):
        print [node, node.left, node.right]
        if node.left is not None:
            self.printNode(node.left)
        if node.right is not None:
            self.printNode(node.right)

    def allNodesRightAreLarger(self):
        return self.nodes_right_larger_helper(self.root.right)

    def nodes_right_larger_helper(self, node):
        if node is None:
            return True
        if node.data < self.root.data:
            return False
        else:
            if self.nodes_right_larger_helper(node.left) is False:
                return False

            if self.nodes_right_larger_helper(node.right) is False:
                return False
            else:
                return True

    def nodes_left_are_smaller(self):
        return self.nodes_left_are_smaller_helper(self.root.left)

    def nodes_left_are_smaller_helper(self, node):
        if node is None:
            return True

        if node.data > self.root.data:
            return False
        else:
            if self.nodes_left_are_smaller_helper(node.left) is False:
                return False
            if self.nodes_left_are_smaller_helper(node.right) is False:
                return False
            else:
                return True

    def tree_min(self, x):
        while x.left is not None:
            x = x.left
        return x

    def tree_max(self, x):
        while x.right is not None:
            x = x.right
        return x
