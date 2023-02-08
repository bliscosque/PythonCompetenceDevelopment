class fenwick_tree:
    def __init__(self,n):
        self.n=n+1 # 1-based index
        self.fn=[0]*self.n
    def add(self,x,y):
        x+=1
        while x<self.n:
            self.fn[x]+=y
            x+=(x&(-x)) # add last set bit with x
    def _sum(self,x):
        x+=1
        ans=0
        while x:
            ans+=self.fn[x]
            x-=(x&(-x))
        return ans
    def sum(self,l,r):
        return self._sum(r)-self._sum(l-1)    

a=[1,2,3,4,5,6,7]
ft=fenwick_tree(len(a))
for i in range(len(a)):
    ft.add(i,a[i])
print(ft.sum(3,4))
print(ft.sum(3,5))
ft.add(4,-3)
print(ft.sum(3,5))