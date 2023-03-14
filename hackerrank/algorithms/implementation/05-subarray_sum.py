def birthday(s, d, m):
    n=len(s)
    if n<m: return 0
    sParc=sum(s[0:m])
    ans=0
    if sParc==d: ans+=1
    for i in range(m,n):
        sParc+=s[i]-s[i-m]
        if sParc==d: ans+=1
    return ans

    
print(birthday([2,2,1,3,2],4,2)) #2 (2 2 / 1 3)
print(birthday([1,2,1,3,2],3,2)) 
print(birthday([1,1,1,1,1,1],3,2)) 
print(birthday([4],4,1)) 