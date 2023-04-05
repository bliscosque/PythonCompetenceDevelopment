def stones(n, a, b):
    ans=set()
    for i in range(n):
        #print(n-i-1,i)
        ans.add((n-i-1)*a+i*b)
    #print(ans)
    return sorted(list(ans))

print(stones(3,1,2))
print(stones(4,10,100))