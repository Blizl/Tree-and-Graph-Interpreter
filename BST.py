#pylint: disable=C0111
#pylint: disable=R0201


class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node data is %s" %(self.data)


class BST(object):
    def insert(self, node, value):
        if node is None:
            return Node(value, None, None)
        if node.data > value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)
        return node

    def search(self, node, value):
        if node.data == value:
            return True
        if node is None:
            return False
        if node.data > value:
            self.search(node.left, value)
        else:
            self.search(node.right, value)

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
        if node.left ^ node.right:
            return True
        else:
            return False
