import sys, math, random
from collections import deque

class Graph:
    def __init__(self,vertices):
        self.vertices = [i+1 for i in range(vertices)]
        self.generateAdjacencyMatrix(vertices)
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
        self.edgeType = 'undirected'
    def deg(self,v):
        if v-1 < 0 or v-1 >= len(self.edges):
            raise Exception("Provided vertex doesn't exist")
        k = 0
        N = len(self.vertices)
        for i in range(N):
            if self.edges[v] != 0:
                k += 1
    def createVertex(self):
        for i in self.edges:
            i.append(0)
        self.edges.append([0 for _ in range(len(self.edges)+1)])
        self.vertices.append(len(self.edges)-1)
    def addUndirectedEdge(self,u,v,weight=1):
        if u-1<0 or u-1 > len(self.edges):
            raise Exception("Provided vertice(s) do not exist in the graph")
        if v-1<0 or v-1 > len(self.edges):
            raise Exception("Provided vertice(s) do not exist in the graph")
        self.edges[u-1][v-1] = weight
        self.edges[v-1][u-1] = weight
    def addDirectedEdge(self,u,v,weight=1):
        if u-1<0 or u-1 > len(self.edges):
            raise Exception("Provided vertice(s) do not exist in the graph")
        if v-1<0 or v-1 > len(self.edges):
            raise Exception("Provided vertice(s) do not exist in the graph")
        self.edgeType = 'directed'
        self.edges[u-1][v-1] = weight
    def removeEdge(self,u,v,removeBoth=False):
        if not u in self.vertices or not v in self.vertices:
            raise Exception("Provided vertice(s) do not exist in the graph")
        self.edges[u-1][v-1] = 0
        if removeBoth==True:
            self.edges[v-1][u-1] = 0
    def isEdge(self,u,v):
        if not u in self.vertices or not v in self.vertices:
            raise Exception("Provided vertice(s) don't exist")
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
            path = [origin]
            while q:
                k = q.pop()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.appendleft(i)
                        path.append(i+1)
            return path
        elif type=='dft':
            q = [origin]
            v = set([origin])
            path = [origin]
            while q:
                k = q.pop()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.append(i)
                        path.append(i+1)
            return path
    def search(self,origin,target,type='bft'):
        if origin-1 < 0 or origin-1 >= len(self.edges):
            raise Exception("Provided origin vertex does not exist.")
        if type=='bft':
            q = deque([origin])
            v = set([origin])
            path = [origin]
            while q:
                k = q.pop()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.append(i)
                        path.add(i+1)
                        if i+1==target:
                            return path
            return [-1]
        elif type=='dft':
            q = [origin]
            v = set([origin])
            path = [origin]
            while q:
                k = q.pop()
                for i in range(len(self.edges[k])):
                    if not i+1 in v:
                        v.add(i+1)
                        q.append(i)
                        path.add(i+1)
                        if i+1==target:
                            return path
            return [-1]
        else:
            raise Exception("Invalid traversal type.")
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
    def generateLaplacianMatrix(self, degreeMatrix):
        #LaplacianMatrix = degreeMatrix - adjacencyMatrix
        if len(degreeMatrix) != len(self.edges):
            raise Exception("Degree matrix and adjacency matrix mismatch. Check what edges and/or vertices you've added.")
        N = len(self.vertices)
        L = [[[0] for _ in range(N)] for __ in range(N)]
        for i in range(N):
            for j in range(N):
                L[i][j] = degreeMatrix[i][j] - self.edges[i][j]
        return L
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
            return D
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
                return None
            return D
        else:
            raise Exception("self.edgeType is undefined, likely because you haven't initialized an adjacency matrix.")
    def generateRandomGraph(self,isAcyclic,isWeighted,connectionType,allowSelfPath=False,lowerBound=1,upperBound=64,disjointPossible=True):
        if lowerBound>upperBound:
            raise Exception("lowerBound for generation of random graph must be greater than upperBound")
        if lowerBound<1:
            raise Exception("lowerBound must be larger than 0")
        V = random.randrange(lowerBound+1,upperBound)
        A = [[0 for _ in range(V)] for __ in range(V)]
        B = random.randrange(lowerBound,V)
        for i in range(7):
            y1 = random.randrange(0,V-1)
            x1 = random.randrange(0,V-1)
            W = random.randrange(1,512)
            if connectionType=='undirected':
                A[y1][x1] = W
                A[x1][y1] = W
            elif connectionType=='directed':
                A[y1][x1] = W
        self.edges = A
        self.vertices = [i+1 for i in range(V)]
        self.edgeType = connectionType
    def generateSpanningTree(self):
        #Prims algorithm
        src = self.vertices[0]
        mstSet = set([src])


