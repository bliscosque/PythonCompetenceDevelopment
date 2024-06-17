def dfs_cycle_undirected(graph, vertex, visited, parent):
    visited[vertex]=True

    for ngb in graph[vertex]:
        if not visited[ngb]:
            if dfs_cycle_undirected(graph,ngb,visited,vertex):
                return True
        elif ngb != parent: 
            return True
    return False

def has_cycle_undirected(graph):
    visited={vertex: False for vertex in graph}

    for vertex in graph:
        if not visited[vertex]:
            if dfs_cycle_undirected(graph,vertex,visited,None):
                return True
    
    return False

graph={
    0: [2],
    1: [2,3],
    2: [1,4,0],
    3: [1,4],
    4: [3,2]
}


print(has_cycle_undirected(graph))

graph2={
    0: [2],
    1: [2,3],
    2: [1,0],
    3: [1,4],
    4: [3]
}
print(has_cycle_undirected(graph2))