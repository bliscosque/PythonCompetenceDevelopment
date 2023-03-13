# Input: sorted array of ints, rotated about a pivot point
# find idx of given elem

def findRotated(arr, key):
    n=len(arr)
    s=0
    e=n-1
    
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==key: return mid # find!

        if arr[s]<=arr[mid]:
            if key>=arr[s] and key<=arr[mid]: e=mid-1 #elem is to left
            else: s=mid+1 # elem is to right
        else:
            if key>=arr[mid] and key <=arr[e]: s=mid+1
            else: e=mid-1
    
    return -1 # not find

a=[7,9,10,1,2,3,4,5,6]
print(findRotated(a,4)) #6
print(findRotated(a,0)) #-1 