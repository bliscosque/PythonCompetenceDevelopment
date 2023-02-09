import math
p,a,b,c,d,n=[int(i) for i in input().split()]
prices=[]
for k in range(n):
    price=p*(math.sin(a*k+b)+math.cos(c*k+d)+2)
    prices.append(price)
maxsofar=prices[0]
maxdecline=0
for i in range(1,len(prices)):
    maxsofar=max(maxsofar,prices[i])
    maxdecline=max(maxdecline,maxsofar-prices[i])

if maxdecline<0: maxdecline=0
print(maxdecline)