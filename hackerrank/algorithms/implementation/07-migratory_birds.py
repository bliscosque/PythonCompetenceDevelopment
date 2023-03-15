from collections import Counter
def migratoryBirds(arr):
    arr.sort()
    counts=Counter(arr)
    return counts.most_common(1)[0][0]

print(migratoryBirds([1,1,2,2,3]))
print(migratoryBirds([1,4,4,4,5,3]))
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
