def coinChange(totalNumber, coins):
    N=totalNumber
    coins.sort()
    idx=len(coins)-1
    while True:
        coinValue=coins[idx]
        if N>=coinValue:
            print(coinValue)
            N-=coinValue
        if N<coinValue:
            idx-=1
        if N==0: break

coins=[1,2,5,20,50,100]
coinChange(201,coins)