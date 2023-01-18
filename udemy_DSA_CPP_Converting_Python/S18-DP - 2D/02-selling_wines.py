# arr p com preco de n vinhos
# today=year 1. In year y, price is y*p[i]
# want to sell one wine per year, starting this year. 
# can sell either leftmost or rightmost wine
# find max profit

def max_profit_wines(p):
    def int_mp(p,y, l, r,dp={}):
        if (l,r) in dp: return dp[(l,r)]
        n1=r-l+1
        if n1==0: return 0
        if n1==1:
            dp[(l,r)]=y*p[r]
            return dp[(l,r)]
        op1=y*p[l]+int_mp(p,y+1,l+1,r)
        op2=y*p[r]+int_mp(p,y+1,l,r-1)
        dp[(l,r)]=max(op1, op2)
        return dp[(l,r)]
    n=len(p)
    return int_mp(p,1,0,n-1)

print(max_profit_wines([2,3,5,1,4])) #50 = 2*1+4*2+1*3+3*4+5*5