# Count the # of BST that can be formed using N nodes, numbered from 1 to N.

# se eu colocar o ith node como root node, quantas maneiras posso formar os nos de 1..i-1 e i+1..n
# soma, para ith no de 1 a N de f(i-1)*f(n-i)
# base case: f(0)=f(1)=1

def numBST(n):
    dp={}
    def internal(n,dp):
        if n in dp: return dp[n]
        if n in [0,1]: return 1
        if n<0: return 0
        s=0
        for i in range(1,n+1):
            s+=internal(i-1,dp)*internal(n-i,dp)
        dp[n]=s
        return s
    return internal(n,dp)
        


print(numBST(3)) # 5
print(numBST(4)) # 14