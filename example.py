from pygraph import Graph

#Creating a new Graph object
graph = Graph(6)

#Adding three new vertices tagged with the names Alice, Bob, and Casey.
graph.addVertex('Alice')
graph.addVertex('Bob')
graph.addVertex('Casey')

#Adding undirected edges between Alice & Bob, Bob & Casey, Casey & Alice.
graph.addUndirectedEdge('Alice','Bob')
graph.addUndirectedEdge('Bob','Casey')
graph.addUndirectedEdge('Casey','Alice')