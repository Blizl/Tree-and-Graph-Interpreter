import unittest
from GraphClass import Graph, Edge, Vertex

class GraphClassTests(unittest.TestCase):
    def createSampleGraph(self):
        vertices = []
        a_vertex = Vertex('A')
        b_vertex = Vertex('B')
        c_vertex = Vertex('C')
        d_vertex = Vertex('D')
        e_vertex = Vertex('E')
        f_vertex = Vertex('F')
        vertices.append(a_vertex)
        vertices.append(b_vertex)
        vertices.append(c_vertex)
        vertices.append(d_vertex)
        vertices.append(e_vertex)
        vertices.append(f_vertex)
        edges = []
        edges.append(Edge(a_vertex, c_vertex, 1))
        edges.append(Edge(a_vertex, b_vertex, 3))
        edges.append(Edge(b_vertex, d_vertex, 2))
        edges.append(Edge(b_vertex, e_vertex, 2))
        edges.append(Edge(c_vertex, f_vertex, 2))
        edges.append(Edge(c_vertex, a_vertex, 2))
        edges.append(Edge(d_vertex, b_vertex, 2))
        edges.append(Edge(e_vertex, f_vertex, 2))
        edges.append(Edge(e_vertex, b_vertex, 2))
        edges.append(Edge(f_vertex, c_vertex, 2))
        edges.append(Edge(f_vertex, e_vertex, 2))

        graph = Graph(vertices, edges)
        return graph
    def test_all_nodes_visited(self):
        graph = self.createSampleGraph()
        for vertex in graph.getVertices():
           vertex.setVisited(True)
        self.assertTrue(graph.allNodesVisited())
    def test_one_node_visited(self):
        graph = self.createSampleGraph()
        graph.getVertices()[0].setVisited(True)
        self.assertFalse(graph.allNodesVisited())
    def test_contains_cycle(self):
        graph =self.createSampleGraph()
        path = []
        a_vertex = Vertex('A')
        c_vertex = Vertex('C')
        f_vertex = Vertex('F')
        path.append(Edge(a_vertex, c_vertex, 1))
        path.append(Edge(c_vertex, f_vertex, 2))
        self.assertFalse(graph.doesNotCreateCycle(path, Edge(f_vertex, c_vertex, 2)))
        
    def test_does_not_contain_cycle(self):
        graph =self.createSampleGraph()
        path = []
        a_vertex = Vertex('A')
        b_vertex = Vertex('B')
        c_vertex = Vertex('C')
        f_vertex = Vertex('F')
        path.append(Edge(a_vertex, c_vertex, 1))
        path.append(Edge(c_vertex, f_vertex, 2))
        self.assertTrue(graph.doesNotCreateCycle(path, Edge(f_vertex, b_vertex, 2)))

    def test_positive_kruskals_algo(self):
        vertices = [Vertex('A'), Vertex('B'), Vertex('C')]
        edges = [Edge(Vertex('A'), Vertex('B'), 2),
                 Edge(Vertex('B'), Vertex('C'), 1),
                 Edge(Vertex('A'), Vertex('C'), 10)]
        graph = Graph(vertices, edges)
        expected_path = graph.kruskals_algorithm()
        correct_path = [Edge(Vertex('B'), Vertex('C'), 1), Edge(Vertex('A'), Vertex('B'), 2)]
        self.assertEqual(expected_path, correct_path)
    def test_negative_kruskals_algo(self):
        vertices = [Vertex('A'), Vertex('B'), Vertex('C')]
        edges = [Edge(Vertex('A'), Vertex('B'), 2),
                 Edge(Vertex('B'), Vertex('C'), 1),
                 Edge(Vertex('A'), Vertex('C'), 10)]
        graph = Graph(vertices, edges)
        correct_path = graph.kruskals_algorithm()
        incorrect_path = [Edge(Vertex('B'), Vertex('C'), 1), Edge(Vertex('A'), Vertex('B'), 10)]
        self.assertNotEqual(correct_path, incorrect_path)
    def test_edge_equality(self):
        edge1= Edge(Vertex('A'), Vertex('B'), 2)
        edge2= Edge(Vertex('A'), Vertex('B'), 2)
        self.assertEqual(edge1, edge2)