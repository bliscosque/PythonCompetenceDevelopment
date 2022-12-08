def numberFactor(n):
    if n in (0,1,2): return 1
    elif n==3: return 2
    else:
        subp1=numberFactor(n-1)
        subp2=numberFactor(n-3)
        subp3=numberFactor(n-4)
        return subp1+subp2+subp3

print(numberFactor(5))