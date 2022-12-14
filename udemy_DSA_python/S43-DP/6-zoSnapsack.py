class Item:
    def __init__(self, profit, weight):
        self.profit=profit
        self.weight=weight

def zeroOneKnapsack(items, capacity, cur_idx, dp):
    dictKey=str(cur_idx)+str(capacity)
    if capacity<=0 or cur_idx<0 or cur_idx>=len(items):
        return 0
    elif dictKey in dp: return dp[cur_idx]
    elif items[cur_idx].weight<=capacity:
        profit1=items[cur_idx].profit+zeroOneKnapsack(items, capacity-items[cur_idx].weight, cur_idx+1, dp) #include current item
        profit2=zeroOneKnapsack(items, capacity, cur_idx+1, dp) #does not include
        dp[dictKey]=max(profit1, profit2)
        return dp[dictKey]
    else:
        return 0

def zoSnapsackBU(profits, weights, capacity):
    if capacity<=0 or len(profits)==0 or len(weights)!=len(profits): return 0
    nRows=len(profits)+1
    dp=[[0 for i in range(capacity+2)] for j in range(nRows)]
    for row in range(nRows-2,-1,-1):
        for col in range(1,capacity+1):
            profit1=0
            profit2=0
            if weights[row]<=col:
                profit1=profits[row]+dp[row+1][col-weights[row]]
            profit2=dp[row+1][col]
            dp[row][col]=max(profit1,profit2)
    return dp[0][capacity]

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0, {}))
print(zoSnapsackBU([31,26,17,72], [3,1,2,5], 7))