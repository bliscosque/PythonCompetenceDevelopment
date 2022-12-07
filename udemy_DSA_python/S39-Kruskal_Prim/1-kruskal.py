class DisjointSet:
    def __init__(self, vertices):
        self.vertices=vertices
        self.parent={}
        for v in vertices:
            self.parent[v]=v
        self.rank=dict.fromkeys(vertices,0)
    
    def find(self,item):
        if self.parent[item]==item: return item
        else: return self.find(self.parent[item])

    def union(self, x, y):
        xroot=self.find(x)
        yroot=self.find(y)
        if self.rank[xroot]<self.rank[yroot]: self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]: self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]+=1

class Graph:
    def __init__(self, vertices) -> None:
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        self.MST=[]

    def addEdge(self, s, d, w):
        self.graph.append([s,d,w])
    
    def addNode(self,value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print(f'${s} - ${d}: ${w}')

    def kruskalAlg(self):
        i,e=0,0
        ds=DisjointSet(self.nodes)
        self.graph=sorted(self.graph, key=lambda item:item[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x!=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlg()