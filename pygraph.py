import sys, math, random
from collections import deque

#Graph represented with adjacency list

class Graph:
    def __init__(self, name='G'):
        self.edges = {}
        self.name = name
    def getEdges(self) -> dict: 
        return self.edges
    def getAdjacentVertices(self,u) -> list:
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + str(self.name))
        return self.edges[u]
    def addEdge(self,u,v):
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + str(self.name))
        if not v in self.edges:
            raise Exception("Provided vertex " + str(v) + " does not exist in Graph " + str(self.name))
        self.edges[u].append(v)
    def addUndirectedEdge(self,u,v):
        self.addEdge(u,v)
        self.addEdge(v,u)
    def addVertex(self,u):
        if u in self.edges:
            raise Exception("Provided vertex " + str(u) + " already exists in Graph " + str(self.name))
        self.edges[u] = list()
    def removeVertex(self,u):
        if not u in self.edges:
            raise Exception("Provided vertex " + str(u) + " does not exist in Graph " + str(self.name))
        del self.edges[u]
        temp = []
        for i in self.edges:
            for j in range(len(i)):
                if i[j]==u:
                    temp.append(j)
            for j in temp:
                i.pop(j)
