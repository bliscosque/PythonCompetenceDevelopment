def diagonalDifference(arr):
    # Write your code here
    n=len(arr)
    s=0
    for i in range(n):
        print(arr[i][i])
        s+=arr[i][i]
        s-=arr[i][n-i-1]
    return abs(s)

arr=[[1,2,3],[4,5,6],[9,8,9]]
print(diagonalDifference(arr))