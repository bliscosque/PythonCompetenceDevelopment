#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nBin=bin(n)
        return nBin.count('1')==1
        
# @lc code=end

