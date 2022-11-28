#Write a function to find the missing number in a given integer array of 1 to 100.
def missingNumber(myList, totalCount):
    sum1=(1+totalCount)*totalCount/2
    sum2=sum(myList)
    return (int(sum1-sum2))

print(missingNumber([1, 2, 3, 4, 6], 6)) # 5