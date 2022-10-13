global ht1, ht2
global ans
ht1=dict()
ht2=dict()

def count(a,b):
    print(a,b)
    global ans
    if a in ht1: ans+=1
    if b in ht2: ans+=1
    print(ht1, ht2, ans)

nT=int(input())
while nT>0:
    ans=0
    ht1.clear()
    ht2.clear()
    nEl=int(input())
    for _ in range(nEl):
        s=input()
        (a,b)=(s[0], s[1])
        ht1[a]=b
        ht2[b]=a
        count(a,b)
    print(ans)
    nT-=1