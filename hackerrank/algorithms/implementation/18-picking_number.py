from collections import Counter
def pickingNumbers(a):
    ans=0
    c=Counter(a)
    for i in range(100):
        ans=max(ans,c[i]+c[i+1])
    return ans



print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
print(pickingNumbers([4,6,5,3,3,1]))
print(pickingNumbers([1,2,2,3,1,2]))