for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    bits=[]
    sbits=[]
    ans=0
    for el in a:
        bits.append(bin(el).replace("0b", "").zfill(31))
    #print(bits)
    for i in range(31):
        sbits.append(0)
        for j in range(n):
            sbits[i]+=int(bits[j][i])
    #print(sbits)
    for i in range(31):
        if n-sbits[i] <=k:
            k-=(n-sbits[i])
            sbits[i]=n #tudo em 1... ao menos na soma
        if sbits[i]==n:
            ans+=1<<(30-i)
    #print(sbits)
    print(ans)
    #print()