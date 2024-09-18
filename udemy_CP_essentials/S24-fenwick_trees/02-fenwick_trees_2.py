class FenwickTree:
    def __init__(self, n) -> None:
        self.n=n
        self.tree=[0]*(n+1) # 1 indexed

    def update(self,i,delta):
        while i<=self.n:
            self.tree[i]+=delta
            i += i&(-i) # remove all bits, except last one

    def query(self,i):
        total=0
        while i>0:
            total+=self.tree[i]
            i -= i&(-i) #remove last set bit
        return total
    
    def range_query(self,left,right):
        return self.query(right)-self.query(left-1)
    

arr=[1,3,4,8,6,1,4,2]
ft=FenwickTree(len(arr))

# build the tree
for i,v in enumerate(arr,1):
    ft.update(i,v)

print(ft.tree)
print(ft.range_query(8,8)) # idx 8 = 2
print(ft.query(4)) #1+3+4+8=16
print(ft.range_query(2,5)) #3+4+8+6=21

ft.update(3,2) #add 2 to idx 3
print(ft.range_query(3,3)) # idx 3 = 6 (atualizado na query anterior)
print(ft.query(4)) #1+3+6+8=18