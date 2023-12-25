from pygraph import Graph

graph = Graph(6)
graph.generateRandomGraph(False,True,'undirected',False,1,12)
print(graph.edges)
print(graph.traverse(1))