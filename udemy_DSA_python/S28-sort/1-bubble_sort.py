def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]

cList=[2,1,6,3,5,6,88]
bubbleSort(cList)
print(cList)