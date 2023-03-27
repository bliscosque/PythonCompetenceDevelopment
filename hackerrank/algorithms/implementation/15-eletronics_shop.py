def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    ans=-1
    for k in keyboards:
        for d in drives:
            if k+d<=b:
                ans=max(ans,k+d)
    return ans

print(getMoneySpent([40,50,60],[5,8,12],60))
print(getMoneySpent([3,1],[5,2,8],10))
print(getMoneySpent([4],[5],5))