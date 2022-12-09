def numberPathsGivenCost(arr, row, col, cost):
    if cost < 0: return 0
    elif row==0 and col==0:
        if arr[0][0]-cost==0: return 1#chegou no fim com custo esperado
        else: return 0
    elif row==0: return numberPathsGivenCost(arr,0,col-1,cost-arr[row][col])
    elif col==0: return numberPathsGivenCost(arr,row-1,0,cost-arr[row][col])
    else:
        op1=numberPathsGivenCost(arr,row-1,col,cost-arr[row][col])
        op2=numberPathsGivenCost(arr,row,col-1,cost-arr[row][col])
        return op1+op2

TwoDList = [[4,7,1,6],
           [5,7,3,9],
           [3,2,1,2],
           [7,1,6,3]
           ]

print(numberPathsGivenCost(TwoDList, 3,3, 25))
