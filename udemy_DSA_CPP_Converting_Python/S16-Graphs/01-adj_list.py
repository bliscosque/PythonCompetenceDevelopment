#no python, a implementacao mais simples é usando dicionário, 
#chave=nó
#valores=para quais nós esse nó aponta
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
    
g=Graph()
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(2,1)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(2,3)
g.addEdge(3,5)
g.printAdjList()