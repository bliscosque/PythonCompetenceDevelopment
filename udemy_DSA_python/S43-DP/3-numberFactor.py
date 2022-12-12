#top down implementation
def numberFactor(n,dp):
    if n in (0,1,2): return 1
    elif n==3: return 2
    elif n in dp: return dp[n]
    else:
        subp1=numberFactor(n-1, dp)
        subp2=numberFactor(n-3, dp)
        subp3=numberFactor(n-4, dp)
        dp[n]=subp1+subp2+subp3
        return dp[n]

#bottom up
def numberFactorBU(n):
    tempArr=[1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]

print(numberFactor(5, {}))
print(numberFactorBU(5))
