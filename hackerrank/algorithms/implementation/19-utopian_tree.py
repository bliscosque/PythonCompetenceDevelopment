def utopianTree(n):
    if n==0: return 1
    ans=1
    summer=True
    for i in range(n):
        if summer:
            ans*=2
        else: 
            ans+=1
        summer=not summer
    return ans

print(utopianTree(5))