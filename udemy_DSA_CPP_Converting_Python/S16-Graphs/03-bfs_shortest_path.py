#para grafos nao ponderados

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

    def bfs(self,src,dst=-1):
        q=deque() #funcionalidade de um queue
        visited=set() #elementos ja visitados
        dist={k:0 for k in self.dct.keys()} # distancias, iniciando tudo com 0
        parent={k:-1 for k in self.dct.keys()} #parent de cada elem, inicialmente com -1
        q.append(src)
        visited.add(src)
        while (len(q)>0): #enquanto a fila nao estiver vazia
            el=q.popleft() #dequeue
            for nbr in self.dct[el]:
                if (nbr not in visited):
                    q.append(nbr)
                    parent[nbr]=el #foi adicionado a partir deste elem
                    dist[nbr]=dist[el]+1 #distancia anterior +1
                    visited.add(nbr)
        #imprimir shortest path
        for k,v in dist.items():
            print(f'shortest distance to {k} is {v}')
        #imprimir path para dest (se esse vier como param)
        if dst!=-1:
            tmp=dst
            while tmp!=src:
                print(str(tmp) + '--',end='')
                tmp=parent[tmp]
            print(src)

g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(5,6)
g.addEdge(4,5)
g.addEdge(0,4)
g.addEdge(3,4)
g.bfs(1,6)