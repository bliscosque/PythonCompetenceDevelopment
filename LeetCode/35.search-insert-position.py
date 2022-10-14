#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=(l+r)//2
        while l <= r:
            mid=(l+r)//2
            if nums[mid]==target: return mid
            elif nums[mid] > target: r=mid-1
            else: l=mid+1
        if nums[mid] < target: return mid+1
        return mid
        
# @lc code=end

