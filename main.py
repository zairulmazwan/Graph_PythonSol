from Graph import Graph
import Graph as g

my_graph = Graph()
my_graph.create_graph()
print("Dataset: ")
my_graph.print_vertices()
print()

print("Edges for 30: ")
my_graph.print_edges(my_graph.get_vertex(30))
print()

print("Depth First Search Algo 1 Result: ")
my_graph.traverse_DFS_1(60)

print("\nDepth First Search Algo 2 Result: ")
visited = []
res = my_graph.traverse_DFS_2(60, visited)
for i in res:
    print(i.value, end=" ")

print("\nBreath First Search Algo Result: ")
my_graph.traverse_BFS(60)
print()







# ©Zairul Mazwan©