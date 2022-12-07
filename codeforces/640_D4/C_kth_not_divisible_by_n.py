import math
def solve():
    n,k=[int(i) for i in input().split()]
    l=k
    r=k*n
    while l<=r:
        ans=(l+r)//2
        if math.floor(ans/n)==ans-k:
            print(ans)
            return
        elif math.floor(ans/n)>ans-k: l=ans+1
        else: r=ans-1
for _ in range(int(input())):
    solve()