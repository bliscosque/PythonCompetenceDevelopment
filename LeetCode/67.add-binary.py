#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        minLen=min(len(a),len(b))
        if (len(a)==minLen): a='0'*(len(b)-len(a))+a
        else: b='0'*(len(a)-len(b))+b
        print(a,b)
        ans=''
        exp=0
        for i in range(len(a)-1,-1,-1):
            print(a[i], b[i], exp)
            if a[i]=='1' and b[i]=='1' and exp==1:
                exp=1
                ans+='1'
                print('c1')
            elif a[i]=='1' and b[i]=='1':
                exp=1
                ans+='0'
                print('c2')
            elif exp==1 and (a[i]=='1' or b[i]=='1'):
                exp=1
                ans+='0'
                print('c3')
            elif a[i]=='1' or b[i]=='1':
                exp=0
                ans+='1'
                print('c4')
            elif exp==1:
                ans+='1'
                exp=0
                print('c5')
            else:
                exp=0
                ans+='0'
                print('else')
        if exp: ans+='1'
        
        return ans[::-1]

        
# @lc code=end

