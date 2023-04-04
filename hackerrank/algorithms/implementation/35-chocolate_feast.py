def chocolateFeast(n, c, m):
    ans=n//c
    n=n%c
    wrappers=ans
    while (wrappers//m)>=1:
        #print(ans)
        b=wrappers//m
        wrappers=wrappers%m
        ans+=b
        wrappers+=b
        #print('w: '+str(wrappers))
    return ans

print(chocolateFeast(15,3,2))
print(chocolateFeast(10,2,5))
print(chocolateFeast(12,4,4))
print(chocolateFeast(6,2,2))