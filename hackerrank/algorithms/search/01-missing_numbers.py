def missingNumbers(arr, brr):
    for el in arr:
        brr.remove(el)
    brr=list(set(brr))
    brr.sort()
    return brr

arr=[7,2,5,3,5,3]
brr=[7,2,5,4,6,3,5,3]

print(missingNumbers(arr,brr))