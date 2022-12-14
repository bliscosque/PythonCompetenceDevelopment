import math
def solve():
    n,k=[int(i) for i in input().split()]
    if k==1: print(1)
    elif k==n: print(n+1)
    else:
        nGroup=k//(n-1) 
        if k%n==0: nGroup-=1
        ans=n*nGroup+k-(n-1)*nGroup
        print(ans)
        
for _ in range(int(input())):
    solve()