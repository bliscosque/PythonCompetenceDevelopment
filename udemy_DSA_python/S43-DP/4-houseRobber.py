#Top down
def houseRobber(houses, cur_idx, dp):
    if cur_idx>=len(houses): return 0
    else:
        if cur_idx not in dp:
            op1=houses[cur_idx]+houseRobber(houses, cur_idx+2, dp) #steal this house
            op2=0 + houseRobber(houses, cur_idx+1, dp) #skip this house
            dp[cur_idx]= max(op1, op2)
        return dp[cur_idx]

#bottom up
def houseRobberBU(houses, cur_idx):
    tmpArr=[0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):
        tmpArr[i]=max(houses[i]+tmpArr[i+2],tmpArr[i+1])
    return tmpArr[0]

houses=[6,7,1,30,8,2,4]
print(houseRobber(houses,0, {}))
print(houseRobberBU(houses,0))