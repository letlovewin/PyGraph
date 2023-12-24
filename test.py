from pygraph import Graph

graph = Graph()
graph.generateAdjacencyMatrix(6)
graph.addUndirectedEdge(1,5)
graph.addUndirectedEdge(1,2)
graph.addUndirectedEdge(2,3)
graph.addUndirectedEdge(2,5)
graph.addUndirectedEdge(4,5)
graph.addUndirectedEdge(4,3)
graph.addUndirectedEdge(4,6)

graph.generateDegreeMatrix()
graph.generateLaplacianMatrix()
print(graph.laplacianMatrix)