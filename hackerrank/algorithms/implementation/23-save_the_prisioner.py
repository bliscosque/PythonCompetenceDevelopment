import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    pos=(s+m-1)
    if pos>n: 
        pos=(pos-1)%n+1
    return pos

    # for i in range(m-1):
    #     s+=1
    #     if s==n+1: s=1
    # return s
        


print(saveThePrisoner(5,2,1))
print(saveThePrisoner(5,2,2))
print(saveThePrisoner(4,6,2)) # 3
print(saveThePrisoner(7,19,2))
print(saveThePrisoner(3,7,3))
print(saveThePrisoner(499999999,999999997,2))
print(saveThePrisoner(499999999,999999998,2))
print(saveThePrisoner(999999999,999999999,1))
