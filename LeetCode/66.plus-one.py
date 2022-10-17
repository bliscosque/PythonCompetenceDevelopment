#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numS=''.join(str(e) for e in digits)
        num=int(numS)
        num+=1
        digits=[int(x) for x in str(num)]
        return digits
        
# @lc code=end

