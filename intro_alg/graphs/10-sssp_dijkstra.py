import heapq

def dijkstra(graph, start):
    n=len(graph)
    distances=[float('inf')]*n
    distances[start]=0
    pq=[(0,start)] #priority queue (distance,vertex)
    heapq.heapify(pq)
    visited=set()

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)
        
        if cur_vertex in visited: 
            continue

        visited.add(cur_vertex)

        for ngb, weight in graph[cur_vertex]:
            distance=cur_dist+weight
            if distance<distances[ngb]:
                distances[ngb]=distance
                heapq.heappush(pq,(distance,ngb))
    
    return distances

graph={
    0: [(3,6),(2,6)],
    1: [(0,3)],
    2: [(3,1)],
    3: [(1,1)],
    4: [(1,4),(3,2)]
}

print(dijkstra(graph,0))