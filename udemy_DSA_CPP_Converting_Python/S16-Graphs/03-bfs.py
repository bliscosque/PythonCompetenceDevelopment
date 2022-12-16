#grafo usando 01_adj_list
from collections import deque
class Graph:
    def __init__(self):
        self.dct={}
    
    def addEdge(self,i,j,undir=True):
        if i not in self.dct: self.dct[i]=[j]
        else: self.dct[i].append(j)
        if (undir): 
            if j not in self.dct: self.dct[j]=[i]
            else: self.dct[j].append(i)
        
    def printAdjList(self):
        print(self.dct)

    def bfs(self,src):
        q=deque() #funcionalidade de um queue
        visited=set() #elementos ja visitados
        q.append(src)
        visited.add(src)
        while (len(q)>0): #enquanto a fila nao estiver vazia
            el=q.popleft() #dequeue
            print(el) 
            for nbr in self.dct[el]:
                if (nbr not in visited):
                    q.append(nbr)
                    visited.add(nbr)

g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(5,6)
g.addEdge(4,5)
g.addEdge(0,4)
g.addEdge(3,4)
g.bfs(1)