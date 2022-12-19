class Graph:
    def __init__(self):
        self.dct={}
    
    def addEdge(self,i,j,undir=True):
        if i not in self.dct: self.dct[i]=[j]
        else: self.dct[i].append(j)
        if (undir): 
            if j not in self.dct: self.dct[j]=[i]
            else: self.dct[j].append(i)

    def dfsHelper(self, node, visited):
        visited[node]=True
        print(f'{node},', end='')
        for nbr in self.dct[node]:
            if visited[nbr]==False:
                self.dfsHelper(nbr,visited)
        return
    
    def dfs(self, src):
        visited={k:0 for k in self.dct.keys()}
        self.dfsHelper(src,visited)

g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(5,6)
g.addEdge(4,5)
g.addEdge(0,4)
g.addEdge(3,4)
g.dfs(1)