def check(l,s):
    #print(l,s)
    sS=s.split('W')
    for sub in sS:
        if len(sub)==0: continue
        if sub.count('R')==0 or sub.count('B')==0: 
            #print(sub, sub.count('R'),sub.count('B'))
            print("NO")
            return
    print("YES")

nT=int(input())
while nT>0:
    l=int(input())
    s=input()
    check(l,s)
    nT-=1