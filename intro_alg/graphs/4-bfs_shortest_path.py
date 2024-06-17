from collections import deque
def bfs_shortest_path(graph,start,goal):
    queue=deque([start])
    visited=set([start])
    predecessor={start:None}

    while queue:
        vertex=queue.popleft()
        if vertex==goal:
            path=[]
            while vertex is not None:
                path.append(vertex)
                vertex=predecessor[vertex]
            path.reverse()
            return path
        
        for ngb in graph[vertex]:
            if ngb not in visited:
                visited.add(ngb)
                predecessor[ngb]=vertex
                queue.append(ngb)
        
    return None # not reachable


graph={
    0: [2],
    1: [2,3],
    2: [1,4,0],
    3: [1,4],
    4: [3,2]
}
print(bfs_shortest_path(graph,3,0))