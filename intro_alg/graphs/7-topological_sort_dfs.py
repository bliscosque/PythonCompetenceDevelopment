def topological_sort_dfs(graph):
    visited={vertex:False for vertex in graph}
    stack=[]

    def dfs(vertex):
        visited[vertex]=True

        for ngb in graph[vertex]:
            if not visited[ngb]:
                dfs(ngb)

        stack.append(vertex)
    
    for vertex in graph:
        if not visited[vertex]:
            dfs(vertex)
    
    return stack[::-1]

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0,1],
    5: [0,2]
}

print(topological_sort_dfs(graph))
