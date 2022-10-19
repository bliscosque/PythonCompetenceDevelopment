def maxSumSubarray(A, n):
    ans=A[0]
    sum=0
    for i in range(n):
        sum+=A[i]
        if sum > ans: ans=sum
        if sum < 0: sum=0
    return ans

A=[5,-6,3,4,-2,3,-3]
print(maxSumSubarray(A, len(A)))