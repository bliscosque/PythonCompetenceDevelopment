from collections import Counter

def equalizeArray(arr):
    counts=Counter(arr)
    mc=counts.most_common(1)
    return len(arr)-mc[0][1]

print(equalizeArray([1,2,2,3]))
print(equalizeArray([3,3,2,1,3]))
print(equalizeArray([1,2,3,1,2,3,3,3]))