import math

n_tea=int(input())
p_tea=[int(i) for i in input().split()]
n_top=int(input())
p_top=[int(i) for i in input().split()]
min_price=math.inf
for i in range(n_tea):
    tea_top=[int(i) for i in input().split()]
    for j in range(1,len(tea_top)):
        #print(i,j)
        #print(p_tea[i]+p_top[tea_top[j]-1])
        min_price=min(min_price,p_tea[i]+p_top[tea_top[j]-1])
#print(min_price)
money=int(input())
ans=money//min_price-1
if (ans>=0):
    print(ans)
else:
    print(0)