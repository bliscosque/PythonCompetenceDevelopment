def solve():
    n=int(input())
    a=[0]
    a+=[int(i) for i in input().split()]
    #print(a)
    cross=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==j): continue
            if (i>j and a[i]<=a[j]) or (i<j and a[i]>=a[j]):
                #print(f'{a[i]} <-> {i} | {a[j]} <-> {j}') 
                cross+=1
    print(cross//2)

for _ in range(int(input())):
    solve()