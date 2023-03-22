from collections import Counter 
def sockMerchant(n, ar):
    counts=Counter(ar)
    ans=0
    for c in counts.values():
        ans+=c//2
    return ans

        
    

print(sockMerchant(7,[1,2,1,2,1,3,2]))
print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))