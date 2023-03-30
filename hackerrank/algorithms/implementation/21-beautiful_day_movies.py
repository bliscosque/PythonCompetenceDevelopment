def beautifulDays(i, j, k):
    ans=0
    for n in range(i,j+1):
        rev_n=int(str(n)[::-1])
        d=abs(rev_n-n)
        #print(n,rev_n,d)
        if d%k==0: ans+=1
    return ans

print(beautifulDays(20,23,6))