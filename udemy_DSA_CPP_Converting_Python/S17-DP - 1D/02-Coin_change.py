# Given an array of coin denomination, and integer M (target money). Find the min coins required to make the change
import math

def coinChange(coins,M):
    dp={i:1 for i in coins}    

    def coinChange_int(coins,M,dp):
        if M in dp: return dp[M]
        if M < 0: return math.inf
        min_v=math.inf
        for coin in coins:
            # Opc2: fazer chamada recursiva apenas se M-coin>0
            min_v=min(min_v,1+coinChange_int(coins,M-coin,dp))
        dp[M]=min_v
        return min_v

    return coinChange_int(coins,M,dp)

def coinChange_BU(coins,M):
    dp=[math.inf]*(M+1)
    dp[0]=0
    for i in range(1,M+1):
        for coin in coins:
            if i-coin>=0: dp[i]=min(dp[i],dp[i-coin]+1)
    
    return dp[M]

coins=[1,3,7,10]
M=15
print(coinChange(coins,M)) #3=7+7+1
print(coinChange_BU(coins,M))
print(coinChange_BU(coins,8))