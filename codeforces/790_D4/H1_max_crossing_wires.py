def solve():
    n=int(input())
    a=[0]
    a+=[int(i) for i in input().split()]
    #print(a)
    cross=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==j): continue
            if a[i]>=i and a[j]<=j and i <= j:
                #print(f'{a[i]} <-> {i} | {a[j]} <-> {j}') 
                cross+=1
    print(cross)

for _ in range(int(input())):
    solve()