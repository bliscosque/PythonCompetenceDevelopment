# given n non-neg integers representing an elevation map where the width of each bar is 1, 
# compute how much water can be trap after raining

def trappedWater(heights):
    n=len(heights)
    if n<=2: return 0
    left=[0]*n
    right=[0]*n
    left[0]=heights[0]
    right[n-1]=heights[n-1]

    for i in range(1,n):
        left[i]=max(left[i-1],heights[i])
        right[n-i-1]=max(right[n-i],heights[n-i-1])

    water=0
    for i in range(n):
        water+=min(left[i],right[i])-heights[i]

    return water

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappedWater(heights))