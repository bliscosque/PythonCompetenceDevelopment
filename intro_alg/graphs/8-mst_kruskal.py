# from disjoint_set_union
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x,root_y=self.find(x),self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x,root_y=root_y,root_x
            self.parent[root_y]=root_x
            if self.rank[root_x]==self.rank[root_y]:
                self.rank[root_x]+=1

    def connected(self,x,y):
        return self.find(x)==self.find(y)

def kruskal(edges,n):
    edges.sort(key=lambda x:x[2])
    uf=UnionFind(n)
    mst=[]
    for u,v,weight in edges:
        if not uf.connected(u,v):
            uf.union(u,v)
            mst.append((u,v,weight))
    return mst

edges= [
    (0, 1, 1), # 0->1 / weight=1
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 6),
    (2, 3, 2)
]

print(kruskal(edges,4)) 