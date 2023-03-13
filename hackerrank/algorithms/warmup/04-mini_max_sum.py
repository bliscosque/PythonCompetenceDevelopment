def miniMaxSum(arr):
    arr.sort()
    smin=sum(arr[0:4])
    smax=sum(arr[1:5])
    print(smin,smax)

arr=[1,3,5,7,9]
miniMaxSum(arr)