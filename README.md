
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

