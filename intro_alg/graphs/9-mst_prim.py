import heapq

def prim(graph):
    mst=[]
    start_node=next(iter(graph)) # um nó para iniciar
    
    #start min heap with ngbs of start node
    edge_min_heap=[(weight,start_node,to_node) for to_node,weight in graph[start_node]]
    visited=set([start_node])

    while edge_min_heap:
        weight, from_node, to_node = heapq.heappop(edge_min_heap)
        if to_node not in visited:
            visited.add(to_node)
            mst.append((from_node,to_node,weight))
        
        for next_node,next_weight in graph[to_node]:
            if next_node not in visited:
                heapq.heappush(edge_min_heap, (next_weight,to_node,next_node))

    return mst

# ALTERAR E TESTAR!!!
graph= {
    0: [(1,1), (2,3)], # 0->1 / weight=1
    1: [(2,1), (3,6)],
    2: [(3,2)],
    3: []
}

print(prim(graph)) 