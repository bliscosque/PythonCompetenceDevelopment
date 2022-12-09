def linSearch(arr, value):
    for i in range(len(arr)):
        if arr[i]==value: return i
    return -1

print(linSearch([20,30,50,10],50))