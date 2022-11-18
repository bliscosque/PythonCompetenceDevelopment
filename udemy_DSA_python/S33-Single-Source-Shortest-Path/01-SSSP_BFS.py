class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1] #last elem
            if node==end: #chegou ao fim
                return path
            for adj in self.gdict.get(node,[]):
                new_path=list(path)
                new_path.append(adj)
                queue.append(new_path)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

graph = Graph(customDict)
print(graph.gdict)
print(graph.bfs("a","f"))