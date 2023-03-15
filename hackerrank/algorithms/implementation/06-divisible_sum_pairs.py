def divisibleSumPairs(n, k, ar):
    ans=0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                #print(ar[i], ar[j], ar[i]+ar[j]) 
                ans+=1
    return ans

print(divisibleSumPairs(6,5,[1,2,3,4,5,6])) # 3
print(divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2]))