class Item:
    def __init__(self, profit, weight):
        self.profit=profit
        self.weight=weight

def zeroOneKnapsack(items, capacity, cur_idx):
    if capacity<=0 or cur_idx<0 or cur_idx>=len(items):
        return 0
    elif items[cur_idx].weight<=capacity:
        profit1=items[cur_idx].profit+zeroOneKnapsack(items, capacity-items[cur_idx].weight, cur_idx+1) #include current item
        profit2=zeroOneKnapsack(items, capacity, cur_idx+1) #does not include
        return max(profit1, profit2)
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0))