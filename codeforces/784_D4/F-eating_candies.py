def check(n,l):
    s1=[l[0]]
    s2=[l[n-1]]
    for i in range(1,n):
        s1.append(s1[i-1]+l[i])
        s2.append(s2[i-1]+l[n-i-1])
    #print(s1, s2)
    i=0
    j=0
    max=0
    while i<(n-j-1):
        if (s1[i]==s2[j]): 
            max=i+j+2
            i+=1
            j+=1
        elif (s1[i]<s2[j]): i+=1
        else: j+=1
    print(max)


nT=int(input())
while nT>0:
    nEl=int(input())
    els=input();
    l=list(map(int,els.split()))
    check(nEl,l)
    nT-=1