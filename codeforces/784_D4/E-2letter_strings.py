nT=int(input())
while nT>0:
    m=[]
    ans=0
    m = [[0]*15 for i in range(15)]
    nEl=int(input())
    for _ in range(nEl):
        s=input()
        (a,b)=(ord(s[0])-ord('a'), ord(s[1])-ord('a'))
        #print ("testing:",a,b)
        for t in range(15):
            if m[t][b] and t!=a: ans+=m[t][b]
            if m[a][t] and t!=b: ans+=m[a][t]
        #print("pans",ans)
        m[a][b]+=1 # adiciona o elemento atual
    print(ans)
    nT-=1