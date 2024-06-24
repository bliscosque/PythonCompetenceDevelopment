class Solution:
    def cutRodBU(self, price, n):
        prices=[0]+price
        profits=[0]*(n+1)
        for len_rod in range(1,n+1):
            max_profit=0
            for len_cut in range(1,len_rod+1):
                max_profit=max(max_profit, prices[len_cut]+profits[len_rod-len_cut])
            profits[len_rod]=max_profit
        print(profits)
        return profits[n]
        


s=Solution()
print(s.cutRodBU([1, 5, 8, 9, 10, 17, 17, 20],8))
print(s.cutRodBU([3, 5, 8, 9, 10, 17, 17, 20],8))