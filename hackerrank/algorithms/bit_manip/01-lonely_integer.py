def lonelyinteger(a):
    ans=0
    for i in a:
        ans=ans^i
    return ans

print(lonelyinteger([1,2,3,4,3,2,1]))
print(lonelyinteger([1]))
print(lonelyinteger([1,1,2]))
print(lonelyinteger([0,0,1,2,1]))