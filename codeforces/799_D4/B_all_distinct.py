from collections import Counter
def solve():
    n=int(input())
    a=[int(i) for i in input().split()]
    c=Counter(a)
    #print(c)
    s_exc=0
    for count in c.values():
        s_exc+=(count-1)
    ans=n-s_exc
    if s_exc%2==1: 
        ans-=1
    print(ans)

for _ in range(int(input())):
    solve()