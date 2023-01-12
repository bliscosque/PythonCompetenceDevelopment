def solve():
    a,b,c,d=[int(i) for i in input().split()] # poderia utilizar unpacking
    ans=0
    if b>a: ans+=1
    if c>a: ans+=1
    if d>a: ans+=1
    print(ans)

for _ in range(int(input())):
    solve()