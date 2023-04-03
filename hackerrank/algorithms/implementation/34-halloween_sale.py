def howManyGames(p, d, m, s):
    ans=0
    while(s>=p):
        s-=p
        ans+=1
        if p-d>=m: p=p-d
        else: p=m
    return ans
    
print(howManyGames(20,3,6,70))
print(howManyGames(20,3,6,80))
print(howManyGames(20,3,6,85))