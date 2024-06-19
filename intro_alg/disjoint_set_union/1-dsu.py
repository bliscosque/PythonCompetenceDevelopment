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

dsu=UnionFind(5)
dsu.union(0,1)
dsu.union(1,2)
dsu.union(3,4)

print(dsu.connected(0,2)) # True
print(dsu.connected(0,3)) # False
