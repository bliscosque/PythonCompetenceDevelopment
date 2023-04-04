import math
def squares(a, b):
    ans=0
    a1=math.floor(a**(1/2))
    b1=math.ceil(b**(1/2))
    for i in range (a1,b1+1):
        if a<=i*i<=b: ans+=1
    return ans

print(squares(24,49)) 
print(squares(3,9)) 
print(squares(17,24)) 
