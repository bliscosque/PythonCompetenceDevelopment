# uma corda de tamanho N pode ser cortada e vendida em suas "partes" (inteiras)
# dado o valor de venda de cada tamanho, calcular o valor max de venda
import math

def cut_rod(vals,n,dp):
    if n in dp: return dp[n]
    if n==0: return 0
    max_v=-math.inf
    for i in range(1,n+1):
        if n-i>=0:
            max_v=max(max_v, vals[i]+cut_rod(vals,n-i,dp))
    dp[n]=max_v
    return max_v

def cut_rod_BU(vals,n):
    dp=[0]*(n+1)
    for len in range(1,n+1):
        ans=-math.inf
        for i in range(0,len):
            cut=i+1
            cur_ans=vals[i]+dp[len-cut]
            ans=max(cur_ans,ans)
        dp[len]=ans
    return dp[n]

dp={}
vals=[0,1,5,8,9,10,17,17,20]
print(cut_rod(vals,8,dp))

dp={}
vals=[0,3,5,8,9,10,17,17,20]
print(cut_rod(vals,8,dp))


vals=[1,5,8,9,10,17,17,20]
print(cut_rod_BU(vals,8))

vals=[3,5,8,9,10,17,17,20]
print(cut_rod_BU(vals,8))