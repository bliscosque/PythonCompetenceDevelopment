def solve():
    n=int(input())
    a=[int(i) for i in input().split()]
    c=input()
    child={}
    for k,v in enumerate(a):
        el=v-1
        if not el in child:
            child[el]=[k+1]
        else: child[el].append(k+1)
    #print(child)
    sub=[(0,0)]*len(c)
    for i in range(len(c)-1,-1,-1):     
        if c[i]=='W': sub[i]=(1,0)
        else: sub[i]=(0,1)
        # se tem filhos, soma tbm dos filhos
        if i in child:
            for ch in child[i]:
                #print(i)
                #print(sub[i],sub[ch])
                sub[i]=(sub[i][0]+sub[ch][0],sub[i][1]+sub[ch][1])                
    #print(sub)
    ans=0
    for el in sub:
        if el[0]==el[1]: ans+=1
    print(ans)                  


for _ in range(int(input())):
    solve()