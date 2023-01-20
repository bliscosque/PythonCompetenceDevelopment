import sys
import math

sys.setrecursionlimit(10**6)
def solve():
    n,s=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    c=sum(a)
    if c==s: 
        print(0)
        return
    if c<s: 
        print(-1)
        return
    def solve_dp(a,l,r,s,dct={}):
        if l==len(a) or r==-1: return math.inf
        if (l,r) in dct: return dct[(l,r)]
        if s==0: return 0
        if a[l]==0:
            op1=1+solve_dp(a,l+1,r,s, dct)
        else:
            op1=1+solve_dp(a,l+1,r,s-1, dct)
        if a[r]==0:
            op2=1+solve_dp(a,l,r-1,s, dct)
        else:
            op2=1+solve_dp(a,l,r-1,s-1, dct)
        dct[(l,r)]=min(op1,op2)
        #print(dct)
        return dct[(l,r)]
    print(solve_dp(a,0,len(a)-1,c-s))

for _ in range(int(input())):
    solve()