def kaprekarNumbers(p, q):
    ans=[]
    for n in range(p,q+1):
        n2=n**2
        d=len(str(n))
        r=n2%(10**d)
        l=n2//(10**d)
        if r+l==n:
            #print(n,n2,l,r) 
            ans.append(n)
    if len(ans)>0:
        for e in ans: print(e, end=' ')
        print()
    else:
        print('INVALID RANGE')

kaprekarNumbers(1,100)