import sys
from quicksort import QuickSort
from heapsort import HeapSort
from GraphClass import Vertex, Edge, Graph
from AVLTree import AVLTree, AVLNode
from BST import Node, BST
from RedBlackTrees import RedBlackTree, RedBlackNode


class TreeGraphInterpreter(object):
    def __init__(self):
        self.selected = False

    def start(self):
        self.select_topic()
        print "Thanks, come again!"

    def select_topic(self):
        while not self.selected:
            print "What type of problem would you like to solve? Enter numbers please or q to quit"
            print "1. Graph\n2. Trees\n3. Sorting Algorithms"
            topic_choice = raw_input(">")
            if topic_choice == "1":
                self.select_graph()
                self.selected = True
            elif topic_choice == "2":
                self.select_tree()
                self.selected = True
            elif topic_choice == "3":
                self.select_sorting_algo()
                self.selected = True
            elif topic_choice == "q":
                sys.exit()

    def select_graph(self):
        print "What graph problem would you like to solve? Enter numbers please or q to quit"
        print "1. BFS\n2.DFS\n3. Prim's\n4. Kruskal's\n5.Shortest Path (Using Djisktra's)"
        graph_choice = raw_input(">")
        while not self.selected:
            if graph_choice == "1":
                print "Bfs selected"
                graph = self.set_graph()
                self.handle_bfs(graph)
                self.selected = True
            elif graph_choice == "2":
                print "DFS selected"
                graph = self.set_graph()
                self.handle_dfs(graph)
                self.selected = True
            elif graph_choice == "3":
                print "Prims selected"
                graph = self.set_graph(withWeights=True)
                self.handle_prims(graph)
                self.selected = True
            elif graph_choice == "4":
                print "Kruskals selected"
                graph = self.set_graph(withWeights=True)
                self.handle_kruskals(graph)
                self.selected = True
            elif graph_choice == "5":
                print "Shortest path selected"
                graph = self.set_graph(withWeights=True)
                self.handle_shortest_path(graph)
                self.selected = True
            elif graph_choice == "q":
                sys.exit()

    def set_graph(self, withWeights=False):
        print "Please enter the number of vertices:\n"
        num_vertices = raw_input(">")
        print "Please enter the number of edges:\n"
        num_edges = raw_input(">")
        vertices = []
        edges = []
        for i in range(int(num_vertices)):
            print "Please enter the name of the vertex: ", i
            vertex_name = raw_input(">")
            vertices.append(Vertex(vertex_name))
        for j in range(int(num_edges)):
            print "Please enter the name of the first vertex of edge\n"
            first_vertex = raw_input(">")
            print "Please enter the name of the second vertex of edge\n"
            second_vertex = raw_input(">")
            if withWeights:
                print "Please enter edge weight\n"
                edge_weight = raw_input(">")
                edges.append(Edge(Vertex(first_vertex), Vertex(second_vertex), edge_weight))
            else:
                edges.append(Edge(Vertex(first_vertex), Vertex(second_vertex)))
        return Graph(vertices=vertices, edges=edges)

    def handle_dfs(self, g):
        print "Please enter what vertex you want to start from:\n"
        start = raw_input(">")
        print "Your answer is ", g.dfs(Vertex(start))

    def handle_bfs(self, g):
        print "Please enter what vertex you want to start from:\n"
        start = raw_input(">")
        print "Your answer is ", g.bfs(Vertex(start))

    def handle_prims(self, g):
        print "Please enter what vertex you want to start from:\n"
        start = raw_input(">")
        print "Your path is ", g.prims_algorithm(Vertex(start))

    def handle_kruskals(self, g):
        print "Your path is ", g.kruskals_algorithm()

    def handle_shortest_path(self, g):
        print "Enter the start vertex"
        start_vertex = raw_input(">")
        print "Enter the end vertex"
        end_vertex = raw_input(">")
        print "Your answer is ", g.find_shortest_path(Vertex(start_vertex), Vertex(end_vertex))

    def select_tree(self):
        print "What tree problem would you like to solve? Enter numbers please or q to quit"
        print "1. AVL Tree\n2.Binary Search Trees\n3.Red Black Trees\n"
        tree_choice = raw_input(">")
        while not self.selected:
            if tree_choice == "1":
                print 'AVL selected'
                self.handle_avl_tree()
                self.selected = True
            elif tree_choice == "2":
                print "BST selected"
                self.handle_BST()
                self.selected = True
            elif tree_choice == "3":
                print "Red Black tree selected"
                self.handle_rb_tree()
                self.selected = True
            elif tree_choice == "q":
                sys.exit()

    def handle_avl_tree(self):
        print "How many nodes would you like to include in the AVL tree?"
        num_nodes = raw_input(">")
        print "Please enter the root node"
        root_node_data = raw_input(">")
        root_node = AVLNode(data=root_node_data, left=None, right=None, is_root=True)
        avl_tree = AVLTree(root_node)
        for i in range(int(num_nodes) -1):
            print "Please enter node val"
            val = raw_input(">")
            avl_tree.insert(avl_tree.root, val)
        print "Your final avl_tree is, in the form [Current, Left Node, Right Node]\n", avl_tree.printAllNodes()

    def handle_BST(self):
        print "How many nodes would you like to include in the binary search tree?"
        num_nodes = raw_input(">")
        print "Please enter the root node"
        root_node_data = raw_input(">")
        root_node = Node(data=root_node_data, left=None, right=None, is_root=True)
        bst = BST(root_node)
        for i in range(int(num_nodes) -1):
            print "Please enter node val"
            val = raw_input(">")
            bst.insert(bst.root, val)
        print "Your final binary search tree is, in the form [Current, Left Node, Right Node]\n", bst.printAllNodes()

    def handle_rb_tree(self):
        print "How many nodes would you like to include in the red black trees"
        num_nodes = raw_input(">")
        print "Please enter the root node"
        root_node_data = raw_input(">")
        root_node = RedBlackNode(data=root_node_data, color="black", left=None, right=None, is_root=True)
        rbt = RedBlackTree(root_node)
        for i in range(int(num_nodes) -1):
            print "Please enter node val"
            val = raw_input(">")
            rbt.insert(rbt.root, RedBlackNode(data=val, color="red", left=None, right=None))
        print "Your final red black tree is, in the form [Current, Left Node, Right Node]\n", rbt.printAllNodes()

    def select_sorting_algo(self):
        print "What sorting algorithm problem would you like to solve? Enter numbers please or q to quit"
        print "1.Quick Sort\n2.Heap Sort"
        sort_choice = raw_input(">")
        while not self.selected:
            if sort_choice == "1":
                print "Quick sort chosen"
                self.handle_quick_sort()
                self.selected = True
            elif sort_choice == "2":
                print "heap sort chosen"
                self.handle_heap_sort()
                self.selected = True
            elif sort_choice == "q":
                sys.exit()

    def handle_quick_sort(self):
        print "Please enter in your values one by one, when you are done, insert x"
        x = False
        quick_sort_list = []
        while not x:
            val = raw_input(">")
            if val == "x":
                x = True
            else:
                quick_sort_list.append(val)
        q = QuickSort()
        print "You entered ", quick_sort_list
        q.quicksort(quick_sort_list,0,  len(quick_sort_list)-1)
        print "Sorted is ", quick_sort_list

    def handle_heap_sort(self):
        print "Please enter in your values one by one, when you are done, insert x"
        x = False
        heap_sort_list = []
        while not x:
            val = raw_input(">")
            if val == "x":
                x = True
            else:
                heap_sort_list.append(val)
        h = HeapSort()
        print "You entered ", heap_sort_list
        h.heapsort(heap_sort_list)
        print "Sorted is ", heap_sort_list

if __name__== "__main__":
    interpreter = TreeGraphInterpreter()
    interpreter.start()
