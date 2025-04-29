
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:

    def __init__(self):
        self.vertices = []

    def add_vertex(self, v):
        self.vertices.append(v)

    def set_edge(self, v1, v2):

        if v1 not in v2.edges:
            v2.edges.append(v1)

        if v2 not in v1.edges:
            v1.edges.append(v2)

    def get_vertex(self, value):

        res = None
        for i in self.vertices:
            if i.value == value:
                res = i
        return res

    # This function is to be used in print_edges
    def get_edges(self, vertex):

        index = self.vertices.index(vertex)
        res = self.vertices[index].edges
        return res

    def print_edges(self, vertex):

        edges = self.get_edges(vertex) # We first need to get the edges by calling the function in line 34
        for i in edges: # We read the elements (vertex) in the edges variable
            print(i.value,end=" ")


    def print_vertices(self):

        for i in self.vertices:
            print(i.value, end=" ")


    def contain_vertex(self, value):

        res = False
        for i in self.vertices:
            if i.value == value:
                res = True
        return res


    def traverse_DFS_2(self, value, visited):

        if self.contain_vertex(value):
            v = self.get_vertex(value)
            if v not in visited:
                visited.append(v)

            for i in v.edges:
                if i not in visited:
                    visited.append(i)
                    self.traverse_DFS_2(i.value, visited)
        else:
            print("There is not vertex in the graph")
        return visited


    def traverse_DFS_1(self, value):
        if self.contain_vertex(value):
            first_node = self.get_vertex(value)
            nodes = []
            nodes.append(first_node)

            visited = []
            while nodes:
                n = nodes.pop()

                if not (n in visited):
                    print(n.value, end=" ")
                    visited.append(n)
                    e = self.get_edges(n)
                    for i in e:
                        nodes.append(i)
        else:
            print("There is no such node in the graph")

    def traverse_BFS(self, value):

        if self.contain_vertex(value):

            start_vertex = self.get_vertex(value)
            queue = []
            queue.append(start_vertex)
            visited = []

            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    print(vertex.value, end=" ")
                    visited.append(vertex)
                    edges = self.get_edges(vertex)
                    for e in edges:
                        queue.append(e)
        else:
            print("There is no vertex in the graph")


    def create_graph(self):

        # Creating vertices using a for loop: 10,20,...60
        for i in range(1,7):
            value = 10*i # i: 1, 2, 3...6
            v = Vertex(value) # Creating a vertex: calling the Vertex class. We set the value first, by default the adges list is empty
            self.add_vertex(v) # Adding the vertex to the graph property i.e., vertices

        # [10,20,30,40,50,60]

        # Edges for 10: 20 and 50 (Refer the function at line 17)
        self.set_edge(self.vertices[0],self.vertices[1]) # Vertex 10 in the list is at index 0, Vertex 20 in the list is at index 1
        self.set_edge(self.vertices[0], self.vertices[4]) # Vertex 10 in the list is at index 0, Vertex 50 in the list is at index 4

        # Edges for 20: 10, 30 and 60 (Refer the function at line 17)
        self.set_edge(self.vertices[1], self.vertices[0]) # Vertex 20 in the list is at index 1, Vertex 10 in the list is at index 0
        self.set_edge(self.vertices[1], self.vertices[2]) # Vertex 20 in the list is at index 1, Vertex 30 in the list is at index 2
        self.set_edge(self.vertices[1], self.vertices[5]) # Vertex 20 in the list is at index 1, Vertex 60 in the list is at index 5

        # Edges for 30: 20, 40 and 50 (Refer the function at line 17)
        self.set_edge(self.vertices[2], self.vertices[1])
        self.set_edge(self.vertices[2], self.vertices[3])
        self.set_edge(self.vertices[2], self.vertices[4])

        # Edges for 40: 30 (Refer the function at line 17)
        self.set_edge(self.vertices[3], self.vertices[2])

        # Edges for 50: 10 and 30 (Refer the function at line 17)
        self.set_edge(self.vertices[4], self.vertices[0])
        self.set_edge(self.vertices[4], self.vertices[2])

        # Edges for 60: 20 (Refer the function at line 17)
        self.set_edge(self.vertices[5], self.vertices[1])


def print_vertices(graph):
    for i in graph:
        print(i.value, end=" ")


# ©Zairul Mazwan©