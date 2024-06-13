def dfs(G,start):
    stack=[start] # stack with start elem
    visited=set([start]) 

    while stack:
        vertex=stack.pop()
        print(vertex, end=" ")
        
        for ngb in G[vertex]:
            if ngb not in visited:
                visited.add(ngb)
                stack.append(ngb)

graph={
    0: [2],
    1: [2,3],
    2: [1,4,0],
    3: [1,4],
    4: [3,2]
}
dfs(graph,1)