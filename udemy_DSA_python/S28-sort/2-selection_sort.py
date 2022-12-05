def selectionSort(customList):
    for i in range(len(customList)):
        min_idx=i
        for j in range(i+1, len(customList)):
            if customList[min_idx] > customList[j]: min_idx=j
        customList[i],customList[min_idx]=customList[min_idx],customList[i]

cList=[2,1,6,3,5,6,88]
selectionSort(cList)
print(cList)
