def dfs_rec(G,vertex,visited=None):
    if visited is None: visited=set()
    visited.add(vertex)

    print(vertex, end=" ")
    
    for ngb in G[vertex]:
        if ngb not in visited:
            dfs_rec(G,ngb,visited)

graph={
    0: [2],
    1: [2,3],
    2: [1,4,0],
    3: [1,4],
    4: [3,2]
}
dfs(graph,1)