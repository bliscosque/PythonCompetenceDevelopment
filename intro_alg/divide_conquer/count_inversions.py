def sort_count_inversions(arr): # returns (sorted, #inversions)
    if len(arr)<=1:
        return (0,arr)
    
    mid=len(arr)//2
    
    B,x=sort_count_inversions(arr[:mid]) #left
    C,y=sort_count_inversions(arr[mid:]) #right

    D,z=merge_count(B,C)

    return (D,x+y+z)

def merge_count(left,right):
    print(left,right)
    result=[]
    i,j=0,0
    inversions=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            inversions+=(len(right)-j)
            j+=1
    result.extend(left[i:])
    result.extend(left[j:])
    return (result, inversions)

print(sort_count_inversions([1,3,5,2,4,6])) #3 (3,2) (5,2) (5,4)