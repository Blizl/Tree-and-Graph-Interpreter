from BST import BST
from BST import Node


class AVLNode(Node):
    def __init__(self, data, left, right, is_root=False, parent=None):
        super(AVLNode, self).__init__(data, left, right, is_root, parent)
        self._balance_factor = 0

    @property
    def balance_factor(self):
        return self._balance_factor

    @balance_factor.setter
    def balance_factor(self, value):
        self._balance_factor = value


class AVLTree(BST):
    def __init__(self, root):
        super(AVLTree, self).__init__(root)

    def insert(self, node,  value):
        if node is None:
            node = AVLNode(value, None, None, False, None)
        else:
            if node.data > value:
                if node.left is None:
                    node.left = AVLNode(value, None, None, False, node)
                    self.update_balance(node.left)
                else:
                    self.insert(node.left, value)
            else:
                if node.right is None:
                    node.right = AVLNode(value, None, None, False, node)
                    self.update_balance(node.right)

                else:
                    self.insert(node.right, value)




    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor +=1
            elif node.is_right_child():
               node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)


    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.right_rotate(node.right)
                self.left_rotate(node)
            else:
                self.left_rotate(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.left_rotate(node.left)
                self.right_rotate(node)
            else:
                self.right_rotate(node)


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
        old_root.balance_factor = old_root.balance_factor -1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor -1 + min(old_root.balance_factor, 0)

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
        old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)
