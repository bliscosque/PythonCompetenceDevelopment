import math
def minimumAbsoluteDifference(arr):
    arr.sort()
    ans=math.inf
    for i in range(0,len(arr)-1):
        ans=min(ans,abs(arr[i]-arr[i+1]))
    return ans


print(minimumAbsoluteDifference([3,-7,0]))
print(minimumAbsoluteDifference([-59,-36,-13,1,-53,-92,-2,-96,-54,75]))
print(minimumAbsoluteDifference([1,-3,71,68,17]))