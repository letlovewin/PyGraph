
# PyGraph

Graph theory library for Python3 for a mathematics/competitive programming use case.

## Usage/Examples

```python
from pygraph import Graph

#Creating a new Graph object
graph = Graph()

#Adding three new vertices tagged with the names Alice, Bob, and Casey.
graph.addVertex('Alice')
graph.addVertex('Bob')
graph.addVertex('Casey')

#Adding undirected edges between Alice & Bob, Bob & Casey, Casey & Alice.
graph.addUndirectedEdge('Alice','Bob')
graph.addUndirectedEdge('Bob','Casey')
graph.addUndirectedEdge('Casey','Alice')

#Doing a depth-first traversal from Alice
depthFirstTraversal = graph.depthFirstTraversal('Alice')
print(depthFirstTraversal)

#Generating an adjacency matrix for the graph
A = graph.generateAdjacencyMatrix()
M = A[0] # A[0] is the adjacency matrix. 
Map = A[1] # A[1] is the mapping that allows you to read the matrix, in the case of you having vertices with string values.
for i in range(len(M)): #Printing the adjacency matrix
    for j in range(len(M)):
        print(M[i][j], end=' ')
    print('')
print(Map) #Printing the mapping from the vertex names to rows & columns of the matrix

#Generating a directed acyclic graph (DAG) and creating a topological sort using Kahn's algorithm
G_2 = Graph('G_2')

G_2.addVertex("Moreno Valley")
G_2.addVertex("Riverside")
G_2.addVertex("San Bernardino")

G_2.addEdge("Moreno Valley", "Riverside")
G_2.addEdge("Riverside", "San Bernardino")

topologicalSorting = G_2.generateTopologicalSorting()

for vertex in topologicalSorting:
    print(vertex, end=' ')
print('')
```

To use this on your own machine, run

```bash
git clone https://github.com/letlovewin/PyGraph.git
```

and just drag pygraph.py into your own project.

