#baseado em grokking alg
from collections import deque

graph={}
graph[0]=[1,3,4]
graph[1]=[]
graph[2]=[]
graph[3]=[2]
graph[4]=[]

def bfs(elem=0):
    search_queue=deque()
    search_queue+=graph[elem]
    searched=set()
    while search_queue:
        el=search_queue.popleft()
        if el not in searched:
            print("searched: ", el)
            search_queue+=graph[el]
            searched.add(el)

bfs()