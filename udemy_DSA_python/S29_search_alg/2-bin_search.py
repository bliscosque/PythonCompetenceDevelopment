def binSearch(arr, value):
    start=0
    end=len(arr)-1
    middle=(start+end)//2
    while arr[middle]!=value and start<=end:
        if value<arr[middle]:
            end=middle-1
        else:
            start=middle+1
        middle=(start+end)//2
    if arr[middle]==value:
        return middle
    else: return -1

print(binSearch([10,11,13,15],13))
print(binSearch([10,11,13,15],0))