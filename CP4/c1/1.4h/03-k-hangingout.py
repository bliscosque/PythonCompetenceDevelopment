L,x=[int(i) for i in input().split()]
cur=0
ans=0
for _ in range(x):
    t,v=input().split()
    v=int(v)
    if t=='enter':
        if cur+v>L:
            ans+=1
        else: cur+=v
    else:
        cur-=v
print(ans)