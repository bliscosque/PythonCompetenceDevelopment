#User function Template for python3

import sys
sys.setrecursionlimit(3000)
class Solution:
    def cutRod(self, price, n):
        prices=[0]+price
        maxprices={0:0}

        def cutRodInt(n):
            if n in maxprices:
                return maxprices[n]
            
            max_price=0
            for i in range(1,n+1):
                if i>n: 
                    break
                max_price=max(max_price,prices[i]+cutRodInt(n-i))
            
            maxprices[n]=max_price
            return maxprices[n]

        return cutRodInt(n)


s=Solution()
print(s.cutRod([1, 5, 8, 9, 10, 17, 17, 20],8))
print(s.cutRod([3, 5, 8, 9, 10, 17, 17, 20],8))