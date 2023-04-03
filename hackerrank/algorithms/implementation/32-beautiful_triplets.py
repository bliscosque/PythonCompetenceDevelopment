def beautifulTriplets(d, arr):
    ans=0
    n=len(arr)
    for i in range(n-2):
        for j in range(i+1,n-1):
            if arr[j]-arr[i]==d:
                for k in range(j+1,n):
                    if arr[k]-arr[j]==d:
                        ans+=1
    return ans

print(beautifulTriplets(1,[2,2,3,4,5]))
print(beautifulTriplets(3,[1, 2, 4, 5, 7, 8, 10]))