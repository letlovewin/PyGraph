import sys
from collections import deque

class Graph:
    def __init__(self,vertices=[],edges=[]):
        self.vertices = vertices
        self.degreeMatrix = None
        self.laplacianMatrix = None
        if edges==[]:
            self.generateAdjacencyMatrix(len(vertices))
        else:
            self.edges = edges
        self.completeness = (len(self.edges))==((1/2)*(len(self.edges)*(len(self.edges)-1)))
        self.edgeDirectionType()
    def edgeDirectionType(self):
        N = len(self.vertices)
        self.edgeType = 'undirected'
        for i in range(N):
            for j in range(N):
                if self.edges[i][j] != self.edges[j][i]:
                    self.edgeType = 'directed'
    def generateAdjacencyMatrix(self,vertices):
        self.vertices = [i+1 for i in range(vertices)]
        self.edges = [[0 for _ in range(vertices)] for __ in range(vertices)]
        self.completeness = False
        self.degreeMatrix = None
        self.laplacianMatrix = None
        self.edgeType = ''
    def deg(self,v):
        if v < 0 or v >= len(self.edges):
            raise Exception("Provided vertex doesn't exist")
        return len(self.edges[v])
    def createVertex(self):
        for i in self.edges:
            i.append(0)
        self.edges.append([0 for _ in range(len(self.edges)+1)])
        self.vertices.append(len(self.edges)-1)
    def addUndirectedEdge(self,u,v,weight=1):
        if u < 0 or u > len(self.vertices):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
            self.vertices.append(u)
        if v < 0 or v > len(self.vertices):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
            self.vertices.append(v)
        #Dynamic resizing of adjacency matrix if u or v isn't in our set of vertices.
        self.edges[u-1][v-1] = weight
        self.edges[v-1][u-1] = weight
    def addDirectedEdge(self,u,v,weight=1):
        self.edgeType = 'directed'
        if not u in self.vertices:
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
            self.vertices.append(u)
        if not v in self.vertices:
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
            self.vertices.append(v)
        #Dynamic resizing of adjacency matrix if u or v isn't in our set of vertices.
        self.edges[u-1][v-1] = weight
    def removeEdge(self,u,v,removeBoth=False):
        if not u in self.vertices or not v in self.vertices:
            raise Exception("Provided vertice(s) do not exist in the graph.")
        self.edges[u-1][v-1] = 0
        if removeBoth==True:
            self.edges[v-1][u-1] = 0
    def isEdge(self,u,v):
        if not u in self.vertices or not v in self.vertices:
            raise Exception("Provided vertice(s) don't exist.")
        if self.edges[u-1][v-1] != 0:
            return True
        else:
            return False
    def isComplete(self):
        N = len(self.edges)
        result = N==((1/2)*(N*(N-1)))
        self.completeness = result
        return result
    def traverse(self,origin,type='bft'):
        if origin-1 < 0 or origin-1 >= len(self.edges):
            raise Exception("Provided origin vertex does not exist.")
        if type=='bft':
            q = deque([origin])
            v = set([origin])
            while q:
                k = q.popleft()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.appendleft(i)
            return v
        elif type=='dft':
            q = [origin]
            v = set([origin])
            while q:
                k = q.pop()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.append(i)
            return v
    def minDistance(self,dist,sptSet):
        min = sys.maxsize
        min_index = 0
        for u in range(len(self.edges)):
            if dist[u] < min and sptSet[u]==False:
                min = dist[u]
                min_index = u
        return min_index
    def djikstra(self,origin,showPath=False):
        if origin-1 > len(self.edges):
            return -1
        path = [origin]
        dist = [sys.maxsize]*len(self.edges)
        dist[origin-1] = 0
        sptSet = [False]*len(self.edges)
        for cout in range(len(self.edges)):
            x = self.minDistance(dist,sptSet)
            sptSet[x] = True
            for y in range(len(self.edges)):
                if self.edges[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.edges[x][y]:
                    dist[y] = dist[x] + self.edges[x][y]
                    path.append(y+1)
        if showPath==False:
            return dist
        else:
            return path
    def generateTopologicalSort(self): #Kahn's algorithm for topological sorting
        N = len(self.vertices)
        in_degree = [0]*N
        for i in range(N):
            for j in self.edges:
                if j[i]!=0:
                    in_degree[i] += 1
        queue = deque()
        for i in range(N):
            if in_degree[i]==0:
                queue.append(i)
        cnt = 0
        top_sort = []
        while queue:
            u = queue.popleft()
            top_sort.append(u+1)
            for i in range(N):
                if self.edges[u][i] != 0:
                    in_degree[i] -= 1
                    if in_degree[i]==0 and i!=u:
                        queue.append(i)
            cnt += 1
        if cnt!=N:
            return([-1])
        return top_sort
    def generateLaplacianMatrix(self):
        #LaplacianMatrix = degreeMatrix - adjacencyMatrix
        if not self.degreeMatrix:
            raise Exception("Degree matrix for this graph hasn't been initialized. Run graph.generateDegreeMatrix()")
        if not self.edges:
            raise Exception("Adjacency matrix for this graph hasn't been intialized. Run graph.generateAdjacencyMatrix() or add some edges.")
        if len(self.degreeMatrix) != len(self.edges):
            raise Exception("Degree matrix and adjacency matrix mismatch. Check what edges and/or vertices you've added.")
        N = len(self.vertices)
        L = [[[0] for _ in range(N)] for __ in range(N)]
        for i in range(N):
            for j in range(N):
                L[i][j] = self.degreeMatrix[i][j] - self.edges[i][j]
        self.laplacianMatrix = L
    def generateDegreeMatrix(self,degreeType='indegree'):
        if self.edgeType == 'undirected':
            D = []
            N = len(self.vertices)
            for i in range(N):
                D.append([0 for _ in range(N)])
            for i in range(N):
                for j in range(N):
                    if self.edges[i][j] != 0:
                        D[i][i] += 1
            self.degreeMatrix = D
        elif self.edgeType == 'directed':
            D = [[[0] for _ in range(len(self.vertices))] for __ in range(len(self.vertices))]
            N = len(self.vertices)
            if degreeType=='outdegree':
                for i in range(N):
                    for j in range(N):
                        if self.edges[i][j] != 0:
                            D[i][i] += 1
            elif degreeType=='indegree':
                for i in range(N):
                    for j in range(N):
                        if self.edges[i][j] != 0:
                            D[j][j] += 1
            else:
                raise Exception("degreeType is invalid. Must be either 'indegree' or 'outdegree'")
                return
            self.degreeMatrix = D
            return
        else:
            self.edgeDirectionType() #run it again if edge direction type hasn't been updated
            self.generateDegreeMatrix()
    def generateSpanningTree(self):
        #Prims algorithm
        src = self.vertices[0]
        mstSet = set([src])


