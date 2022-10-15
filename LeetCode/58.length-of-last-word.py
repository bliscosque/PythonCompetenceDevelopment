#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        for i in range(n-1,-1,-1):
            if (s[i]!=' '): 
                n=i
                break
        count=0
        for i in range(n,-1,-1):
            if (s[i]!=' '): count+=1
            else: break
        return count

        
# @lc code=end

