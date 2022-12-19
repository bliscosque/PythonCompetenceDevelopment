#Using DFS

class Graph:
    def __init__(self):
        self.dct={}
    
    def addEdge(self,i,j,undir=True):
        if i not in self.dct: self.dct[i]=[j]
        else: self.dct[i].append(j)
        if (undir): 
            if j not in self.dct: self.dct[j]=[i]
            else: self.dct[j].append(i)

    def dfs(self, node, visited, parent):
        visited[node]=True
        for nbr in self.dct[node]:
            if visited[nbr]==False:
                nbrFoundCycle=self.dfs(nbr,visited,node)
                if nbrFoundCycle: return True
            elif nbr!=parent: return True
        return False

    def contains_circle(self):
        visited={k:False for k in self.dct.keys()}
        return self.dfs(0,visited,-1)

g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
print(g.contains_circle())