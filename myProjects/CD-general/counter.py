from collections import Counter
nums=[0,0,0,2,3,3,3,3,11,11,1,2]
counts=Counter(nums)
print(counts)
print(counts.most_common(2))