def balancedSums(arr):
    if len(arr)==1: return 'YES'
    idx=0
    sl=0
    sr=sum(arr)-arr[0]
    while idx<len(arr)-1:
        if sl==sr: return 'YES'
        idx+=1
        sl+=arr[idx-1]
        sr-=arr[idx]
    return 'NO'


print(balancedSums([1,2,3]))
print(balancedSums([1,2,3,3]))
print(balancedSums([1,1,4,1,1]))
print(balancedSums([2,0,0,0]))
print(balancedSums([0,0,2,0]))