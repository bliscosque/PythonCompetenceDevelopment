def solve():
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    a.sort()
    dct={}
    for el in a:
        if el not in dct:
            dct[el]=1
        else:
            dct[el]+=1
    long=-1
    cnt=0
    min_t=a[0]
    max=a[0]
    for i in range(a[0],a[-1]+1):
        if i in dct and dct[i]>=k:
            cnt+=1
            if cnt==1: min_t=i
        else:
            cnt=0
        if cnt>long:
            long=cnt
            min=min_t
            max=i
    if long>0: print(min,max)
    else: print(-1)

for _ in range(int(input())):
    solve()