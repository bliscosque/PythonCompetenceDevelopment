def getTotalX(a, b):
    start=max(a)
    end=min(b)
    ans=0
    for i in range(start,end+1):
        isValid=True
        for el in a:
            if i%el!=0: 
                isValid=False
                break
        if not isValid: continue
        for el in b:
            if el%i!=0:
                isValid=False
                break
        if isValid: ans+=1
    return ans

print(getTotalX([2,6],[24,36]))#2 (6 and 12)
print(getTotalX([2,4],[16,32,96]))