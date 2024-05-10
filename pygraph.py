import sys, math, random
from collections import deque

#Graph represented with adjacency list

class Graph:
    #Let G = {V,E}
    #E is given when the class is initialized. V is just inferred from E, since E is just an adjacency list in this instance.
    def __init__(self, name='G'):
        self.edges = {}
        self.name = str(name)

    def setName(self, name):
        self.name = str(name)

    def getEdges(self) -> dict: 
        """
        :return: The adjacency list for the graph.
        :rtype: dictionary
        """
        return self.edges
    
    def deg(self,u, type="in") -> int:
        """
        :param u: The vertex provided by the user.
        :param type: The type of the degree that's wanted, either "in" or "out"
        :return: deg(u)
        :rtype: int
        """
        if type=="in":
            temp_deg = 0
            for i in self.edges:
                for j in self.edges[i]:
                    if j[0]==u:
                        temp_deg += 1
            return temp_deg
        elif type=="out":
            return len(self.edges[u])
        else:
            raise Exception("The provided degree type for Graph " + self.name + " does not exist.")
        
    
    def getAdjacentVertices(self,u) -> list:
        """
        :param u: The vertex provided by the user.
        :return: The adjacent edges of u.
        :rtype: list
        :raises Exception: if u doesn't actually exist within the graph.
        """
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + self.name)
            return
        return self.edges[u]
    
    def addEdge(self,u,v,w=1):
        """
        :param u: The origin vertex
        :param v: The vertex that u connects to.
        :raises Exception: if u doesn't exist within the graph.
        :raises Exception: if v doesn't exist within the graph.
        """
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + self.name)
            return
        if not v in self.edges:
            raise Exception("Provided vertex " + str(v) + " does not exist in Graph " + self.name)
            return
        self.edges[u].append((v,w))

    #Just adds an edge from u -> v and v -> u
    def addUndirectedEdge(self,u,v,w=1):
        """
        :param u: The first vertex.
        :param v: The second vertex.
        :param w: The weight of the edge. Defaults to 1
        """
        self.addEdge(u,v,w)
        self.addEdge(v,u,w)

    #Adds a new vertex to the graph
    def addVertex(self,u):
        """
        :param u: The name of you vertex you want to add.
        """
        if u in self.edges:
            raise Exception("Provided vertex " + str(u) + " already exists in Graph " + self.name)
            return
        self.edges[u] = list()

    #Removes a vertex from the graph and scrubs it from the adjacency list
    def removeVertex(self,u):
        """
        :param u: The vertex you want to delete.
        """
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + self.name)
            return
        del self.edges[u]
        temp = []
        for i in self.edges:
            for j in range(len(i)):
                if i[j]==u:
                    temp.append(j)
            for j in temp:
                i.pop(j)
    
    #DFS function, self explanatory
    def depthFirstTraversal(self,vertex, visited=set()) -> set:
        """
        :param vertex: The source vertex for the DFT
        :param visited: Do not touch if you're not working on the class. This is for recursion
        :return: All vertices accessible from vertex
        :rtype: set
        """
        if vertex not in self.edges:
            raise Exception("Provided vertex " + str(vertex) + " already exists in Graph " + self.name)
            return
        if vertex not in visited:
            visited.add(vertex)
            for n in self.edges[vertex]:
                self.depthFirstTraversal(n[0], visited)
        return visited
    
    #Djikstra's algorithm
    def generateSingleSourceShortestPaths(self,vertex) -> dict:
        """
        :param vertex: The source vertex
        :return: The minimum distance to go from the source vertex to all other vertices in the graph.
        :rtype: dict
        """
        if not vertex in self.edges:
            raise Exception("Provided vertex " + str(vertex) + " already exists in Graph " + self.name)
            return
        
        temp_v = {i:sys.maxsize for i in self.edges}
        temp_v[vertex] = 0

        q = deque([vertex])
        vi = set()

        while q:
            v = q.pop()
            if not v in vi:
                vi.add(v)
                for i in self.edges[v]:
                    temp_v[i[0]] = min(temp_v[i[0]],i[1]+temp_v[v])
                    q.appendleft(i[0])

        for i in temp_v:
            if temp_v[i] == sys.maxsize:
                temp_v[i] = "Unreachable from vertex " + str(vertex)
        return temp_v
    
    #Adjacency matrix
    #Returns two things: the actual adjacency matrix, and a mapping from the names of the vertices to what row and column they would correspond to on the matrix.
    #For example, if we had matrices A, B, and C, it would return a 3x3 matrix as well as a dictionary: {A: 0, B: 1, C: 2}
    def generateAdjacencyMatrix(self) -> tuple[list,dict]:
        """
        :return: The adjacency matrix for the graph, along with a mapping from the vertex names to their indexes on the matrix.
        :rtype: tuple
        """
        N = len(self.edges)

        matrix = []
        mapping = {}
        for i in range(N):
            matrix.append([0 for j in range(N)])

        for index, key in enumerate(self.edges):
            mapping[key] = index

        for vertex in self.edges:
            for adjacentVertex in self.edges[vertex]:
                matrix[mapping[adjacentVertex[0]]][mapping[vertex]] = adjacentVertex[1]

        return (matrix,mapping)

    def generateDegreeMatrix(self, type="out") -> tuple[list,dict]:
        """
        :param type: "out" gives a degree matrix based on outdegrees. "in" gives a degree matrix based on indegrees.
        :return: The degree matrix for the graph.
        :rtype: tuple
        """
        N = len(self.edges)

        matrix = []
        mapping = {}
        for i in range(N):
            matrix.append([0 for j in range(N)])

        for index, key in enumerate(self.edges):
            mapping[key] = index

        if type=="out" or type=="in":
            for vertex in self.edges:
                matrix[mapping[vertex]][mapping[vertex]] = self.deg(vertex,type)
        else:
            raise ValueError("Invalid degree type when generateDegreeMatrix was called for Graph " + self.name)

        return (matrix,mapping)
    
    def generateLaplacianMatrix(self) -> tuple[list,dict]:
        """
        :return: The Laplacian matrix for the graph, which is the degree matix minus the adjacnecy matrix.
        :rtype: tuple
        """
        D = self.generateDegreeMatrix()
        Dm = D[0]

        A = self.generateAdjacencyMatrix()
        Am = A[0]

        Map = D[1]
        N = len(self.edges)

        for i in range(N):
            for j in range(N):
                Dm[i][j] -= Am[i][j]

        return (Dm,Map)

    def generateTopologicalSorting(self) -> list:
        """
        :return: A topological sorting of the graph.
        :rtype: list
        """
        degreeMatrixTuple = self.generateDegreeMatrix("in")
        degreeMatrix = degreeMatrixTuple[0]

        f = degreeMatrixTuple[1]  #f is a mapping from the names of the vertices to integer values. This allows the construction of matrices related to the graph.
        
        inDegreeMap = {vertex: degreeMatrix[f[vertex]][f[vertex]] for vertex in self.edges}
        inDegreeTemp = deque(list())

        topologicalOrder = list()

        for vertex in inDegreeMap:
            if inDegreeMap[vertex] == 0:
                inDegreeTemp.appendleft(vertex) #Finds all vertices that have no other vertices going into them.

        while inDegreeTemp:
            top = inDegreeTemp.pop()
            topologicalOrder.append(top)
            for vertex in self.edges:
                for adjacentVertex in self.edges[vertex]:
                    inDegreeMap[adjacentVertex[0]] -= 1
                    if inDegreeMap[adjacentVertex[0]] == 0:
                        inDegreeTemp.appendleft(adjacentVertex[0])
            
        if len(topologicalOrder) == len(self.edges):
            return topologicalOrder
        else:
            return [-1] #The topological order should have all of the vertices within the graph. If it doesnt' have all vertices within the graph, there's a cycle in the graph, so returning a topological order would be worthless.

        


        



            
