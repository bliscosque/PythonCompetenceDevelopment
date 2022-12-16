#ao invés de representar como uma lista, representando como uma lista da classe "Node"
class Node:
    def __init__(self, name) -> None:
        self.name=name

class Graph:
    def __init__(self, vList) -> None:
        self.dct={}
        for v in vList:
            self.dct[v]=[]
    
    def addEdge(self,i,j,undir=False):
        self.dct[i].append(j)
        if undir: self.dct[j].append(i)

    def printAdjList(self):
        print(self.dct)

cities = ["Delhi","London","Paris","New York"]
g=Graph(cities)

g.addEdge("Delhi","London")
g.addEdge("New York","London")
g.addEdge("Delhi","Paris")
g.addEdge("Paris","New York")

g.printAdjList()