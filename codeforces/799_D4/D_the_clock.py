def ispal(hh,mm):
    return hh[0]==mm[1] and hh[1]==mm[0]

def sumx(hh,mm,x):
    hhI=int(hh)
    mmI=int(mm)
    mmI+=x
    if mmI>59:
        hhI+=mmI//60
        mmI=mmI%60
        if hhI>23:
            hhI=hhI%24
    return (str(hhI).zfill(2), str(mmI).zfill(2))

def solve():
    hhmm,x=[x for x in input().split()]
    x=int(x)
    hh,mm=hhmm.split(":")
    ans=0
    if ispal(hh,mm): ans+=1
    hhN,mmN=sumx(hh,mm,x)
    # print(hhN,mmN)
    while (hhN!=hh or mmN!=mm):
        #print(hhN,mmN)
        if ispal(hhN,mmN): ans+=1
        hhN,mmN=sumx(hhN,mmN,x)
    print(ans)

for _ in range(int(input())):
    solve()