import math
def viralAdvertising(n):
    ans=0
    shared=5
    for d in range(n):
        likes=math.floor(shared//2)
        ans=ans+likes
        shared=likes*3
        
    return ans

print(viralAdvertising(5))
print(viralAdvertising(3))