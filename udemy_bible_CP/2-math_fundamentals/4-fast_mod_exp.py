def fastExp_rec(a,n,mod):
    if n==0: return 1
    if n%2==0: #n eh par
        return fastExp_rec(a*a, n//2, mod)
    return (a*fastExp_rec(a, n-1, mod))%mod

def fastExp_iter(a,n,mod):
    ans=1
    while n>=1:
        if (n%2==0):
            a=(a*a)%mod
            n/=2
        else:
            ans=(ans*a)%mod
            n-=1
    return ans

print(fastExp_rec(5, 64, 19)) # 5
print(fastExp_iter(5, 64, 19)) # 5