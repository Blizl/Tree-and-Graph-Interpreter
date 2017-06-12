from AVLTree import AVLTree
from BST import Node


class RedBlackNode(Node):
    def __init__(self, data, left, right, color, is_root=False, parent=None):
        super(RedBlackNode, self).__init__(data, left, right, is_root, parent)
        self.color = color

    def is_red(self):
        if self.color is "red":
            return True
        else:
            return False

    def is_black(self):
        if self.color is "black":
            return True
        else:
            return False

    def __repr__(self):
        return "(%s, color:%s)" % (self.data, self.color)


class RedBlackTree(AVLTree):
    def __init__(self, root_node):
        super(RedBlackTree, self).__init__(root_node)

    def insert_fixup(self, z):
        while z.parent is not None and z.parent.is_red():
            if z.parent.is_left_child():
                y = z.parent.parent.right
                if y is not None and y.is_red():
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z.is_right_child():
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.is_red():
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z.is_left_child():
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)

        self.root.color = "black"

    def insert(self, root_node, z):
        y = None
        x = self.root
        # leaf_node_1 = RedBlackNNode(None, None, None, "black")
        # leaf_node_2 = RedBlackNNode(None, None, None, "black")
        # z = RedBlackNNode(data, leaf_node_1, leaf_node_2, "red")
        # while x.data is not None:
        while x is not None:
            y = x
            if z.data < x.data:  # The reason why 1 is inserting into the node object is because of this statement
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        # z.left = RedBlackNNode(None, None, None, "black")
        # z.right = RedBlackNNode(None, None, None, "black")
        z.left = None
        z.right = None
        z.color = "red"
        self.insert_fixup(z)

    def right_rotate(self, old_root):
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right = old_root
        new_root.parent = old_root.parent
        if old_root.is_root:
            old_root.is_root = False
            self.root = new_root
            self.root.is_root = True
        if old_root.is_left_child():
            old_root.parent.left = new_root
        else:
            if old_root.parent is not None:
                old_root.parent.right = new_root
        old_root.parent = new_root

    def left_rotate(self, old_root):

        new_root = old_root.right
        old_root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_root:
            old_root.is_root = False
            self.root = new_root
            self.root.is_root = True
        else:
            if old_root.is_left_child():
                old_root.parent.left = new_root
            else:
                old_root.parent.right = new_root
        new_root.left = old_root
        old_root.parent = new_root


    def maintains_rb_properties(self):
        return (self.root.is_black() and self.allNodesRightAreLarger() and self.nodes_left_are_smaller()
                and self.all_red_nodes_have_black_children(self.root) and self.same_num_black_children_per_path())

    def all_red_nodes_have_black_children(self, node):
        if node is None:
            return True
        if node.is_red():
            if node.left is not None and node.left.is_black():
                return self.all_red_nodes_have_black_children(node.left)
            elif node.right is not None and node.right.is_black():
                return self.all_red_nodes_have_black_children(node.right)
            else:
                return False
        else:
            self.all_red_nodes_have_black_children(node.left)
            self.all_red_nodes_have_black_children(node.right)
            return True

    def same_num_black_children_per_path(self):
        return True

    def rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.is_left_child():
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def remove(self, z):
        y = z
        y_original_color = y.color
        if z.left is None:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right is None:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent  =y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color is "black":
            self.remove_fixup(x)

    def remove_fixup(self, x):
        while x is not self.root and x.color is "black":
            if x.is_left_child():
                w = x.parent.right
                if w.color is "red":
                    w.color =  "black"  # Case 1
                    x.parent.color = "red"  # Case 1
                    self.left_rotate(x.parent)  # Case 1
                    w = x.parent.right  # Case 1
                if w.left.color is "black" and w.right.color is "black":
                    w.color = "red"  # Case 2
                    x = x.parent  # Case 2
                elif w.right.color is "black":
                    w.left.color = "black"
                    w.color = "red"
                    self.right_rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = "black"
                w.right.color = "black"
                self.left_rotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.color is "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color is "black" and w.left.color is "black":
                    w.color = "red"
                    x = x.parent
                elif w.left.color is "black":
                    w.right.color = "black"
                    w.color = "red"
                    self.left_rotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                w.parent.color = "black"
                w.left.color = "black"
                self.right_rotate(x.parent)
                x = self.root
        x.color = "black"



