from pygraph import Graph

graph = Graph(6)
graph.addUndirectedEdge(1,2)
graph.addUndirectedEdge(2,3)
#graph.addUndirectedEdge(3,4)
graph.addUndirectedEdge(4,5)
graph.addUndirectedEdge(5,6)
result = graph.findConnectedComponents()
print(result)