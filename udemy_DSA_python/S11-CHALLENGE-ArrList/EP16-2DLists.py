#Given 2D list calculate the sum of diagonal elements.
def sumDiagonal(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i][i]
    return sum


myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
print(sumDiagonal(myList2D)) # 15