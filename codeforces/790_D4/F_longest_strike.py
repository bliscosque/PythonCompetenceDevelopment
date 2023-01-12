def solve():
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    s=set()
    dct={}
    for el in a:
        if el not in dct:
            dct[el]=1
            s.add(el)
        else:
            dct[el]+=1
    long=-1
    cnt=0
    min_el=max_el=-1
    last=-1
    #print(dct)
    
    for i in s:
        if dct[i]>=k:
            if last==-1:
                cnt=1
                min_el=i
                max_el=i
                last=i
            else:
                if last+1==i:
                    cnt+=1
                    max_el=i
                else:
                    cnt=1
                    min_el=i
                    max_el=i
                last=i
        else:
            cnt=0
            min_el=-1
            max_el=-1
        if cnt>long:
            long=cnt
            minAll=min_el
            maxAll=max_el
    if long>0: print(minAll,maxAll)
    else: print(-1)

for _ in range(int(input())):
    solve()