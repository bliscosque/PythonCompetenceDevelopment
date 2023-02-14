import math
p,a,b,c,d,n=[int(i) for i in input().split()]
prices=[]
for k in range(n):
    price=p*(math.sin(a*(k+1)+b)+math.cos(c*(k+1)+d)+2)
    prices.append(price)
maxsofar=prices[0]
maxdecline=0
for i in range(1,len(prices)):
    if maxsofar<prices[i]:
        maxsofar=prices[i]
    elif maxdecline<maxsofar-prices[i]:
        maxdecline=maxsofar-prices[i]

if maxdecline<=0: maxdecline=0.0
print(maxdecline)