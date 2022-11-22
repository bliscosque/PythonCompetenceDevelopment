import heapq
class Edge:
    def __init__(self, weight, start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None # a partir de qual no cheguei aqui?
        self.neighbors=[] # or children
        self.min_distance=float("inf")

    def __lt__(self,other_node): # override <
        return self.min_distance < other_node.min_distance

    def add_edge(self,weight,destination_vertex):
        edge=Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap=[]

    def calculate(self,start_vertex):
        start_vertex.min_distance=0 # os demais já estao com inf
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap) # menor nó
            if actual_vertex.visited: continue # ja visitei esse nó... apenas continue
            for edge in actual_vertex.neighbors:
                start=edge.start_vertex
                target=edge.target_vertex
                new_distance=start.min_distance+edge.weight
                if new_distance < target.min_distance:
                    target.min_distance=new_distance
                    target.predecessor=start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited=True

    def get_shortest_path(self,vertex):
        print(f"Shortest path to vertex os: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name,end=" ")
            actual_vertex=actual_vertex.predecessor


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeB)
print()
algorithm.get_shortest_path(nodeG)
print()
algorithm.get_shortest_path(nodeF)