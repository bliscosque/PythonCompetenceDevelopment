from collections import deque
def bfs(G,start):
    queue=deque([start]) # queue with start elem
    visited=set([start]) 

    while queue:
        vertex=queue.popleft()
        print(vertex, end=" ")
        
        for ngb in G[vertex]:
            if ngb not in visited:
                visited.add(ngb)
                queue.append(ngb)

graph={
    0: [2],
    1: [2,3],
    2: [1,4,0],
    3: [1,4],
    4: [3,2]
}
bfs(graph,1)