import sys
from collections import deque

class Graph:
    def __init__(self,vertices=[],edges=[]):
        self.vertices = vertices
        self.edges = [[0 for _ in range(len(vertices))] for __ in range(len(vertices))]
    def deg(self,v):
        if v < 0 or v >= len(self.edges):
            return -1
        return len(self.edges[v])
    def addUndirectedEdge(self,u,v,weight=1):
        if u > len(self.edges):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
        if v > len(self.edges):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
        #Dynamic resizing of adjacency matrix if u or v isn't in our set of vertices.
        self.edges[u-1][v-1] = weight
        self.edges[v-1][u-1] = weight
    def addDirectedEdge(self,u,v,weight=1):
        if u > len(self.edges):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
        if v > len(self.edges):
            for i in self.edges:
                i.append(0)
            self.edges.append([0 for _ in range(len(self.edges)+1)])
        #Dynamic resizing of adjacency matrix if u or v isn't in our set of vertices.
        self.edges[u-1][v-1] = weight
    def isEdge(self,u,v):
        if u > len(self.edges) or v > len(self.edges):
            return False
        if self.edges[u][v] != 0:
            return True
        else:
            return False
    def traverse(self,origin,type='bft'):
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
