def solve():
    n1,n2,n3=[int(i) for i in input().split()]
    if n2==0:
        if n1==0: 
            ans='1'*(n3+1)
        if n3==0:
            ans='0'*(n1+1)
        print(ans)
    else:
        start=1
        ans=[]
        for _ in range(n2+1):
            ans.append(start)
            start=1 if start==0 else 0
        #print(ans)
        ans=[1]*(n3)+ans
        x=ans.index(0)
        ans=ans[:x]+[0]*(n1)+ans[x:]
        ans=''.join(map(str,ans))
        print(ans)

for _ in range(int(input())):
    solve()