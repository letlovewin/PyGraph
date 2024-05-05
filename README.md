
# PyGraph

Graph theory library for Python3 for a mathematics/competitive programming use case.

## Usage/Examples

```python
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
```

To use this on your own machine, run

```bash
git clone https://github.com/letlovewin/PyGraph.git
```

and just drag pygraph.py into your own project.

