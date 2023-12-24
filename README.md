
# GrayGraph

Graph theory library for Python3 for a mathematics/competitive programming use case. Has BFS/DFS capabilities, uses an adjacency matrix, more to be added.

At the moment, only numerical vertices are compatible with this graph.


## Usage/Examples
Breadth-First Traversal on a graph of 4 vertices.
```python
newGraph = Graph([1,2,3,4])
newGraph.addUndirectedEdge(1,2)
newGraph.addUndirectedEdge(2,3)
newGraph.addUndirectedEdge(3,4)
path = newGraph.traverse(1)
print(path)
```
and with a Depth-First Traversal on the same graph:
```python
newGraph = Graph([1,2,3,4])
newGraph.addUndirectedEdge(1,2)
newGraph.addUndirectedEdge(2,3)
newGraph.addUndirectedEdge(3,4)
path = newGraph.traverse(1,'dft')
print(path)
```
with the first parameter in our function being the source vertex, and the second parameter being the sort of traversal that we want to use (either 'bft' or 'dft').
we also have Djikstra's algorithm, for example on a graph of G = {{1,2,3,4,5},{{1,2,4},{1,3,6},{2,3,10},{3,4,2},{4,1,2},{1,5,10}}}:
```python
  graph = Graph([1,2,3,4,5])
    graph.addDirectedEdge(1,2,4)
    graph.addDirectedEdge(1,3,6)
    graph.addDirectedEdge(2,3,10)
    graph.addDirectedEdge(3,4,2)
    graph.addDirectedEdge(4,1,2)
    graph.addDirectedEdge(1,5,10)
    result = graph.djikstra(4,False)
    print(result)
```
With the first parameter being the source vertex, and the second parameter being whether we want to show exact paths or not.
