def sset(nums):
    n=len(nums)
    for i in range(1<<n): # 0.. n^2-1 in binary
        for j in range(n): # go all elements from binary representation
            if i & (1<<j): # if jth bit is set
                print(nums[j], end=" ")
        print()

sset([0,1,2,3])