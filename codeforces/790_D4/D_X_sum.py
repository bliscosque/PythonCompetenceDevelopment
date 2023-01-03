def check(l,i,j):
    ans=l[i][j]
    dirx=[-1,-1,1,1]
    diry=[-1,1,-1,1]
    for k in range(4):
        m=i+dirx[k]
        n=j+diry[k]
        while m>=0 and n>=0 and m<len(l) and n<len(l[0]):
            ans+=l[m][n]
            m+=dirx[k]
            n+=diry[k]
    #print(i,j,ans)
    return ans

def solve():
    n,m=[int(i) for i in input().split()]
    l=[]
    ans=0
    for _ in range(n):
        l.append([int(i) for i in input().split()])
    for i in range(n):
        for j in range(m):
            ans=max(ans,check(l,i,j))
    print(ans)

for _ in range(int(input())):
    solve()