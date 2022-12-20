class Graph:
    def __init__(self):
        self.dct={}
    
    def addEdge(self,i,j): #insere apenas direcionado
        if i not in self.dct: self.dct[i]=[j]
        else: self.dct[i].append(j)

    def dfs(self, node, visited, stack):
        visited[node]=True
        stack[node]=True
        for nbr in self.dct[node]:
            if stack[nbr]==True: return True
            elif visited[nbr]==False:
                nbrFoundCycle=self.dfs(nbr,visited,stack)
                if nbrFoundCycle: return True
        stack[node]=False
        return False

    def contains_circle(self):
        visited={k:False for k in self.dct.keys()}
        stack={k:False for k in self.dct.keys()}

        for el in self.dct.keys():
            if visited[el]==False:
                if self.dfs(el,visited,stack): return True

        return False

g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
print(g.contains_circle())