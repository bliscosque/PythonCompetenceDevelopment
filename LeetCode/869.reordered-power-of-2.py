#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        #nstr=str(n)
        #perm=permutations(nstr)
        #for i in list(perm):
        #    n=''.join(i)
        #    n=int(n)
        #    if(len(str(n))!=len(i)): continue
        #    if (n and (not(n & (n - 1)))): return True #check if power 2
        #return False
        frN=[0] * 10
        n=str(n)
        for i in n:
            frN[int(i)]+=1
        for i in range(30):
            nTest=str(2**i)
            frTest=[0]*10
            for j in nTest:
                frTest[int(j)]+=1
            if frTest==frN: return True
        return False       

        
# @lc code=end

