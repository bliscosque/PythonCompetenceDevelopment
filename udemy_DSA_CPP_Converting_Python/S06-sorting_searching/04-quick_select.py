# write a function that takes an input array of distinct int and returns the kth smallest in the arr

def quick_select(arr,k):
    #print(arr,k)
    if len(arr)<2: return arr[0]
    else:
        pivot=arr[0]
        less=[i for  i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        if len(less)==k: return pivot
        if len(less)>k:
            return quick_select(less,k)
        return quick_select(greater,k-len(less)-1)

arr=[10,5,2,0,7,6,4]
# print(sorted(arr)) # [0, 2, 4, 5, 6, 7, 10]
print(quick_select(arr,1)) # 6
for i in range(len(arr)):
    print(quick_select(arr,i))