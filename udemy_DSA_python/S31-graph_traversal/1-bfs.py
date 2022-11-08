class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited=[vertex]
        queue=[vertex]
        while (queue):
            deVertex=queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

customDict={"a": ["b", "c"],
            "b": ["a", "d", "e"],
            "c": ["a","e"],
            "d": ["a", "e", "f"],
            "e": ["d", "f"],
            "f": ["d", "e"]
            }

graph = Graph(customDict)
print(graph.gdict)
graph.bfs("a")