n=int(input())
ans=0
for _ in range(n):
    q,y=[float(f) for f in input().split()]
    ans+=q*y
print(ans)