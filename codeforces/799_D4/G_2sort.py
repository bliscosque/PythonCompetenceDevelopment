def solve():
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    ans=0
    for i in range(n-k):
        flag=True
        p=0
        for j in range(k):
            if 2**p*a[i+j]>=2**(p+1)*a[i+j+1]: 
                flag=False
                break
            p*=2
        if flag==True: ans+=1
    print(ans) 

for _ in range(int(input())):
    solve()