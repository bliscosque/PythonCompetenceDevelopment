def cutTheSticks(arr):
    ans=[]
    arr.sort()
    while sum(arr)>0:
        for idx,el in enumerate(arr):
            if el>0:
                m=el
                ans.append(len(arr)-idx)
                break
        for i in range(len(arr)):
            if arr[i]>0: arr[i]-=m
        #print(arr)
        #print(ans)
    return ans


print(cutTheSticks([5, 4, 4, 2, 2, 8]))
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))