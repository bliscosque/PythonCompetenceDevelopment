import math
class Graph:
    def __init__(self,v) -> None:
        self.l=[[] for _ in range(v)] # cada edge é uma tupla peso,proximo nó
    def addEdge(self,u,v,wt,undir=False):  #wt=peso
        self.l[u].append((wt,v))
        if (undir):
            self.l[v].append((wt,u))
    def dijkstra(self,src,dst):
        dist=len(self.l)*[math.inf]
        s=set()

        print(self.l)
        dist[src]=0
        s.add((0,src))
        while (len(s)!=0):
            print(s)
            distTillNow,node=s.pop() #remove and return elem
            print(f"l[node]: {self.l[node]}")
            for wt,nbr in self.l[node]:
                if distTillNow+wt<dist[nbr]:
                    s.discard((dist[nbr],nbr))
                    dist[nbr]=distTillNow+wt
                    s.add((dist[nbr],nbr))
        for i,val in enumerate(dist):
            print(f"Node: {i} has dist: {val}")
        return dist[dst]

g=Graph(5)
g.addEdge(0,1,1)
g.addEdge(1,2,1)
g.addEdge(0,2,4)
g.addEdge(0,3,7)
g.addEdge(3,2,2)
g.addEdge(3,4,3)
print(g.dijkstra(0,4))


