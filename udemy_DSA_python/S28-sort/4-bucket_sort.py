import math
def bucketSort(customList):
    numberOfBuckets=round(math.sqrt(len(customList)))
    maxValue=max(customList)
    arr=[]
    for i in range(numberOfBuckets): # create buckets
        arr.append([])
    for j in customList:
        index_b=math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numberOfBuckets): # ordenar buckets individualmente
        arr[i].sort()
    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1
    return customList

cList=[2,1,6,3,5,6,88]
bucketSort(cList)
print(cList)

