def maxSumSubarrayPartialSum(A, n):
    ans=A[0]
    S=[A[0]] #partial sum
    for i in range(1,len(A)):
        S.append(A[i]+S[i-1])
    minS=0
    for i in range(n):
        if S[i]-minS > ans: ans=S[i]-minS
        if S[i] < minS: minS=S[i]
    return ans

A=[5,-6,3,4,-2,3,-3]
print(maxSumSubarrayPartialSum(A, len(A)))