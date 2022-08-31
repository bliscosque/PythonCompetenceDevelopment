def binary_search(A,i):
    l=0
    r=len(A)-1
    while (l<=r):
        mid=int((l+r)/2)
        if (i==A[mid]):
            return mid
        elif i>A[mid]:
            l=mid+1
        else:
            r=mid-1
    return None

A=[1,2,3,10,11,12]
print(binary_search(A,10))
print(binary_search(A,9))