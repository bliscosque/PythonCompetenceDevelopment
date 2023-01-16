# n stores as array. Each int represent height of the stone
# frog is at stone 1. It can:
# jump to stone i+1, i+2. Cost |h[i]-h[j]|
# find min possible cost to reach last stone
def jumpCost(arr):
    dp={}
    def jumpCost_int(arr):
        n=len(dp)
        if n in dp: return dp[n]
        if len(arr)>2:
            op1=abs(arr[0]-arr[1])+jumpCost(arr[1:])
            op2=abs(arr[0]-arr[2])+jumpCost(arr[2:])
            min_v=min(op1,op2)
        if len(arr)==2:
            min_v=abs(arr[0]-arr[1])
        if len(arr)==1:
            min_v=0
        dp[n]=min_v
        return min_v
    return jumpCost_int(arr)

print(jumpCost([10,10])) # 0

print(jumpCost([30,10,60,10,60,50])) # 40 (1 -> 3 -> 5 -> 6)

print(jumpCost([10,30,40,20])) # 30 