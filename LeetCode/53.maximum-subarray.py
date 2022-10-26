#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        psum=0
        for i in range(len(nums)):
            psum=psum+nums[i]
            if psum > ans: ans=psum
            if psum < 0: psum=0
        return ans
        
# @lc code=end

