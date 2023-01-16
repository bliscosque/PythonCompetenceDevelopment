# given arr of posit int, find the max sum of non-adj elem in the array

import math
def max_non_adj_sum(arr):
    dp={}
    def max_non_adj_int(arr):
        n=len(arr)
        if n in dp: return dp[n]
        max_s=-math.inf
        if n>2:
            for i in range(2,n):
                max_s=max(max_s,arr[0]+max_non_adj_sum(arr[i:]))
        if n==2 or n==1:
            max_s=max(arr)
        dp[n]=max_s
        return max_s
    return max_non_adj_int(arr)


print(max_non_adj_sum([6,10,12,7,9,14])) # 32 (12+6+14)