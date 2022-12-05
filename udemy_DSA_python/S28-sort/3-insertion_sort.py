def insertionSort(customList):
    for i in range(1,len(customList)):
        key=customList[i]
        j=i-1
        while j>=0 and key < customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key

cList=[2,1,6,3,5,6,88]
insertionSort(cList)
print(cList)
