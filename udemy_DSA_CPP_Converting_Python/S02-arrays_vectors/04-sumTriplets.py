def sumTriplets(arr,target_sum):
    n=len(arr)
    arr.sort()
    result=[]
    #2-pointers, para cada elemento...
    for i in range(0,n-2):
        j=i+1
        k=n-1
        while j<k:
            cur_sum=arr[i]
            cur_sum+=arr[j]
            cur_sum+=arr[k]
            if (cur_sum==target_sum):
                result.append((arr[i],arr[j],arr[k]))
                j+=1
                k-=1
            elif cur_sum>target_sum: k-=1
            else: j+=1 
        return result

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
print(sumTriplets(arr,18))