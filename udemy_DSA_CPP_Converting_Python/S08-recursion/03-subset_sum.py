#given a set of non-neg int, and a value sum, determine if there is a subset of the given set with the sum equal to givem sum

def subsetSum(arr,X,i=0):
    n=len(arr)
    if i==n:
        if X==0: return 1
        return 0
    inc=subsetSum(arr,X-arr[i],i+1)
    exc=subsetSum(arr,X,i+1)
    return inc+exc
    


print(subsetSum([10,12,15,6,19,20],16)) # YES=1