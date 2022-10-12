def fastExp_rec(a,n,mod):
    if n==0: return 1
    if n%2==0: #n eh par
        return fastExp_rec(a*a, n//2, mod)
    return (a*fastExp_rec(a, n-1, mod))%mod

print(fastExp_rec(5, 64, 19)) # 5