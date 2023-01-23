# given 2 str, find the # of times the second str occurs as subseq in the first str

def subseq_count(a,b):
    m=len(a)-1
    n=len(b)-1
    def sub_c_int(a,b,m,n, dp={}):
        if (m,n) in dp: return dp[(m,n)]
        if (m==-1 and n==-1) or n==-1: 
            dp[(m,n)]=1
            return 1 
        if m==-1:
            dp[(m,n)]=0
            return 0
        if a[m]==b[n]: # match
            dp[(m,n)]=sub_c_int(a,b,m-1,n-1)+sub_c_int(a,b,m-1,n)
            return dp[(m,n)]
        else:
            dp[(m,n)]=sub_c_int(a,b,m-1,n)
            return dp[(m,n)]
    
    return sub_c_int(a,b,m,n)


# BU approach
# a linha 0 e coluna 0 representam str vazia (sao o relativo ao -1 do código recursivo)
def subseq_count_BU(a,b):
    m=len(a)
    n=len(b)
    dp=[[0]*(n+1)]*(m+1)
    for i in range(m+1):
        dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]

    return dp[m][n]


print(subseq_count("ABCDCE","ABC")) #2
print(subseq_count("ABBCDCE","ABC")) #4
print(subseq_count_BU("ABCDCE","ABC"))
print(subseq_count_BU("ABBCDCE","ABC"))