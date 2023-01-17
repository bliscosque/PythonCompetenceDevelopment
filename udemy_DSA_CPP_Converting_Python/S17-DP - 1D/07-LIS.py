# given array, find the len of longest increasing subseq

# ideia: preencher o dp[i] com 1+max(dp[j]), for 0<=j<i e arr[j]<arr[i]
def lis(arr):
    n=len(arr)
    dp=[1]*n
    for i in reversed(range(n)):
        for j in range(i,n):
            if arr[j]>arr[i]:
                dp[i]=max(dp[i],1+dp[j])
    return max(dp)


print(lis([50,4,10,8,30,100])) # 4 (4,8,30,100)