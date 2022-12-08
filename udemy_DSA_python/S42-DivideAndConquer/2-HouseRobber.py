def houseRobber(houses, cur_idx):
    if cur_idx>=len(houses): return 0
    else:
        op1=houses[cur_idx]+houseRobber(houses, cur_idx+2) #steal this house
        op2=0 + houseRobber(houses, cur_idx+1) #skip this house
        return max(op1, op2)

houses=[6,7,1,30,8,2,4]
print(houseRobber(houses,0))