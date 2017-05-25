from collections import deque
import operator
class Vertex:
    def __init__(self, vertex_name, weight=None, visited=False):
        self.vertex_name = vertex_name
        self.weight = weight
        self.visited = visited
    def __repr__(self):
        return "Vertex %s" % self.vertex_name
    def getVertex(self):
        return self.vertex_name
    def getWeight(self):
        return self.weight
    def isVisited(self):
        return self.visited
    def setVertex(self, vertex):
        self.vertex_name = vertex
    def setWeight(self, weight):
        self.weight = weight
    def setVisited(self, visited):
        self.visited = visited
class Edge:
    def __init__(self, source_vertex, destination_vertex, weight=1, visited=False):
        self.source = source_vertex
        self.destination = destination_vertex
        self.weight = weight
        self.visited = visited
    def __repr__(self):
        return "Edge (%s, %s) weight: %s" %(self.source, self.destination, self.weight)
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def getWeight(self):
        return self.weight
    def isVisited(self):
        return self.visited
    def setSource(self, source):
        self.source = source
    def setDestination(self, destination):
        self.destination = destination
    def setWeight(self, weight):
        self.weight = weight
    def setVisited(self, visited):
        self.visited = visited
class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges
        self.visited = []
        self.stack = []
    def kruskals_algorithm(self):
        path = []
        sorted_edges = self.getSortedEdges()
        while (self.allNodesVisited()):
            for edge in sorted_edges:
                if self.doesNotCreateCycle(path, edge):
                    path.append(edge)
                    sorted_edges.remove(edge)
        return path
    def doesNotCreateCycle(self, path, edge):
        pass
    def allNodesVisited(self):
        for vertex in self.vertices:
            if not vertex.isVisited():
                return False
        return True
    def bfs(self, start):
        self.stack.append(start)
        self.visited.append(start)
        while (len(self.stack) != 0):
            vertex = self.stack.pop()
            for adj_vertex in self.get_adjacent_vertices(vertex):
                if adj_vertex not in self.visited:
                    self.stack.append(adj_vertex)
                    self.visited.append(adj_vertex)
        return self.visited
    def getEdgeWeight(self, source, destination):
        for edge in self.edges:
            if edge.getSource() == source and edge.getDestination() == destination:
                return edge.getWeight()
    def dfs(self, vertex):
        adjacent_vertices = self.get_adjacent_vertices(vertex)
        if adjacent_vertices < self.visited: 
            return None
        else:
            self.visited.append(vertex)
            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex not in self.visited:
                    self.dfs(adjacent_vertex)
            return self.visited
    def prims_algorithm(self):
        pass 

    def find_shortest_path(self, start_vertex, end_vertex):
        distances, prev = self.djisktra(start_vertex) 
        path = []
        vertex = end_vertex
        path.append(vertex)
        while (vertex != start_vertex):
            vertex = prev[vertex]
            path.append(vertex)
        path.reverse()
        return path
    def djisktra(self, start_vertex):
        queue = deque([])
        distances = {}
        prev = {}
        for vertex in self.vertices:
            distances[vertex] = 99999
        queue.append(start_vertex)
        distances[start_vertex] = 0
        while len(queue) > 0:
            vertex = queue.popleft()
            for adj_vertex  in self.get_adjacent_vertices(vertex):
                if distances[adj_vertex] > distances[vertex] +self.getEdgeWeight(adj_vertex, vertex):
                    distances[adj_vertex] = distances[vertex] + self.getEdgeWeight(adj_vertex, vertex)
                    prev[adj_vertex] = vertex
                    queue.append(adj_vertex)
        return distances, prev
    def get_adjacent_vertices(self, vertex):
        adjacent_vertices = []
        for edge in edges:
            if edge.getDestination() == vertex:
                adjacent_vertices.append(edge.getSource())
            elif edge.getSource() == vertex:
                adjacent_vertices.append(edge.getDestination())
        return set(adjacent_vertices)
    def getSortedEdges(self):
        sorted_edges = sorted(self.edges, key=operator.attrgetter('weight'))
        return sorted_edges
    def getVertices(self):
        return self.vertices

vertices = []
a_vertex =Vertex('A')
b_vertex = Vertex('B')
c_vertex = Vertex('C')
d_vertex = Vertex('D')
e_vertex =Vertex('E')
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
# for vertex in graph.dfs(a_vertex):
#     print vertex.getVertex()
# for vertex in graph.bfs(a_vertex):
    # print vertex.getVertex()
# distances = graph.djisktra(a_vertex) TODO: Seems like it's failing again for some reason
# for vertex in distances[0].keys():
#     print vertex.getVertex(), distances[0][vertex]
# for vertex in distances[1].keys():
#     print vertex.getVertex(), distances[1][vertex].getVertex()
# for vertex in graph.find_shortest_path(b_vertex, f_vertex):
#     print vertex

