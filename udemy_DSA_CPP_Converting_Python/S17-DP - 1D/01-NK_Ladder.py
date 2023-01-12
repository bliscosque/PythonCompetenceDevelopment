# Given a ladder of size n, and integer k, write a function to compute # of ways to climb the ladder if you can take a jump of
# atmost k at every step

def ladderNK(n,k):
    dp={}
    
    def ladderNK_int(n,k,dp):
        if n==0: return 1
        if n<0: return 0
        if n in dp: return dp[n]
        sPartial=0
        for i in range(1,k+1):
            sPartial+=ladderNK(n-i,k)
        dp[n]=sPartial
        return dp[n]
    
    return ladderNK_int(n,k,dp)

# bottom up
def ladderNK_BU(n,k):
    dp=[0]*(n+1) # inicializa tbm tudo com 0
    dp[0]=1 # base case dp[0]=1
    for i in range (1,n+1):
        for jump in range(1,k+1):
            if i-jump>=0: dp[i]+=dp[i-jump]
    return dp[n]

print(ladderNK(4,3)) #7
print(ladderNK(6,3)) #24

print(ladderNK_BU(4,3)) #7
print(ladderNK_BU(6,3)) #24