def dfs_cycle_directed(graph, vertex, visited, rec_stack):
    visited[vertex]=True
    rec_stack[vertex]=True

    for ngb in graph[vertex]:
        if not visited[ngb]:
            if dfs_cycle_directed(graph,ngb,visited,rec_stack):
                return True
        elif rec_stack[ngb]:
            return True

    rec_stack[vertex]=False
    return False

def has_cycle_directed(graph):
    visited = {vertex:False for vertex in graph}
    rec_stack = {vertex:False for vertex in graph}

    for vertex in graph:
        if not visited[vertex]:
            if dfs_cycle_directed(graph,vertex,visited,rec_stack):
                return True
    
    return False

graph_directed = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]  
}

print(has_cycle_directed(graph_directed))

graph_directed2 = {
    0: [1],
    1: [3],
    2: [3],
    3: []  
}
print(has_cycle_directed(graph_directed2))