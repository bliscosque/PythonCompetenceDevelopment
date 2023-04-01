def findDigits(n):
    digits=[(int)(i) for i in (str)(n)]
    ans=0
    for d in digits:
        if d==0: continue
        if n%d==0: ans+=1
    return ans

print(findDigits(124))
print(findDigits(111))
print(findDigits(10))