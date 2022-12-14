import math
def solve():
    n,k=[int(i) for i in input().split()]
    nGroup=k//(n-1) 
    if k%n==0: nGroup-=1
    ans=n*nGroup+k-(n-1)*nGroup
    print(ans)
        
for _ in range(int(input())):
    solve()