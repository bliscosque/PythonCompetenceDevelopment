#equivalente ao anterior, mas o próprio nó contem a lista com seus vizinhos (e nao o grafo)
class Node:
    def __init__(self, name) -> None:
        self.nbrs=[]
        self.name=name

class Graph:
    def __init__(self, vList) -> None:
        self.dct={}
        for v in vList:
            self.dct[v]=Node(v)
    
    def addEdge(self,i,j,undir=False):
        self.dct[i].nbrs.append(j)
        if undir: self.dct[j].nbrs.append(i)

    def printAdjList(self):
        for node in self.dct.values():
            print(node.name)
            print(node.nbrs)

cities = ["Delhi","London","Paris","New York"]
g=Graph(cities)

g.addEdge("Delhi","London")
g.addEdge("New York","London")
g.addEdge("Delhi","Paris")
g.addEdge("Paris","New York")

g.printAdjList()