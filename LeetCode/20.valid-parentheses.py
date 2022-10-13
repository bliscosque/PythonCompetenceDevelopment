# @before-stub-for-debug-begin
from python3problem20 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for ch in s:
            if ch in ('(','[','{'):
                l.append(ch)
            else:
                if len(l)==0: return False
                last=l.pop()
                if ch==')':
                    if last!='(': return False
                elif ch==']':
                    if last!='[': return False
                elif ch=='}':
                    if last!='{': return False
        if len(l)==0: return True
        return False

        
# @lc code=end

