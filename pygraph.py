import sys
from collections import deque

class Graph:
    def __init__(self,vertices=[],edges=[]):
        self.vertices = vertices
        if edges==[]:
            self.edges = [[0 for _ in range(len(vertices))] for __ in range(len(vertices))]
        else:
            self.edges = []
        self.completeness = (len(self.edges))==((1/2)*(len(self.edges)*(len(self.edges)-1)))
    def generateAdjacencyMatrix(self,vertices):
        self.edges = [[0 for _ in range(vertices)] for __ in range(vertices)]
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
        self.edges[v-1][u-1] = weight
    def addDirectedEdge(self,u,v,weight=1):
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
    def isEdge(self,u,v):
        if not u in self.vertices or not v in self.vertices:
            raise Exception("Provided vertex doesn't exist.")
        if self.edges[u-1][v-1] != 0:
            return True
        else:
            return False
    def isComplete(self):
        N = len(self.edges)
        return N==((1/2)*(N*(N-1)))
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
    def generateSpanningTree(self):
        #Prims algorithm
        src = self.vertices[0]
        mstSet = set([src])


