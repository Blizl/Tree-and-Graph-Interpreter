
class BinaryTreeTraversals:
    def left(self, node, tree):
        node_index = tree.index(node)
        left_index = 2 *node_index
        if left_index < len(tree):
            return tree[left_index]
        else:
            return None

    def right(self, node, tree):
        node_index = tree.index(node)
        right_index = 2 * node_index + 1
        if right_index < len(tree):
            return tree[right_index]
        else:
            return None

    def has_no_children(self, currentNode, tree):
        if not self.left(currentNode, tree) and self.right(currentNode, tree):
            return True
        else:
            return False

    def in_order(self, visited, tree, current_node, num_nodes):
        if len(visited) == num_nodes:
            return
        if self.has_no_children(current_node, tree):
            return
        else:
            left_node = self.left(current_node, tree)
            right_node = self.right(current_node, tree)
            self.in_order(visited, tree, left_node, num_nodes)
            visited.append(current_node)
            self.in_order(visited, tree, right_node, num_nodes)
        return visited

    def pre_order(self, visited, tree, current_node, num_nodes):
        if len(visited) == num_nodes:
            return
        if self.has_no_children(current_node, tree):
            return
        else:
            left_node = self.left(current_node, tree)
            right_node = self.right(current_node, tree)
            visited.append(current_node)
            self.pre_order(visited, tree, left_node, num_nodes)
            self.pre_order(visited, tree, right_node, num_nodes)
        return visited

    def post_order(self, visited, tree, current_node, num_nodes):
        if len(visited) == num_nodes:
            return
        if self.has_no_children(current_node, tree):
            return
        else:
            left_node = self.left(current_node, tree)
            right_node = self.right(current_node, tree)
            self.post_order(visited, tree, left_node, num_nodes)
            self.post_order(visited, tree, right_node, num_nodes)
            visited.append(current_node)
        return visited

    # def max_path(self, tree, max_weight, current_node):
    #     if self.has_no_children(current_node, tree):
    #         max_weight = current_node.weight
    #     else:
    #         left_node = self.left(current_node,tree)
    #         right_node = self.right(current_node, tree)
    #         max_left = self.max_path(tree, max_weight, left_node)
    #         max_right = self.max_path(tree, max_weight, right_node)
    #         max_weight += max(max_left, max_right)
    #     return max_weight