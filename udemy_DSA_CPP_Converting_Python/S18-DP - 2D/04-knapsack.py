# Given weighs and prices of n items.
# maximize items in a bag of capacity W

def knapsack(n,w,wts,prices,i=0):
    if i>=n or w<=0: return 0
    if w-wts[i] >=0:
        include=prices[i]+knapsack(n,w-wts[i],wts,prices,i+1)
    else: include=0
    exclude=knapsack(n,w,wts,prices,i+1)
    return max(include,exclude)

#not working!!!
def knapsackBU(N,W,wts,prices):
    dp=[[0]*(W+1)]*(N+1)
    for n in range(1,N+1):
        for w in range(1,W+1):
            inc=exc=0
            if wts[n-1]<=w:
                inc=prices[n-1]+dp[n-1][w-wts[n-1]]
            exc=dp[n-1][w]
            dp[n][w]=max(inc,exc)
    print(dp)
    return dp[N][W] 

print(knapsack(4,11,[2,7,3,4],[5,20,20,10]))
print(knapsackBU(4,11,[2,7,3,4],[5,20,20,10]))