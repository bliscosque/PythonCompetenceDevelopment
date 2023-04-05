def fairRations(B):
    ans=0
    for i in range(len(B)-1):
        if B[i]%2==1:
            B[i]+=1
            B[i+1]+=1
            ans+=2
    if B[-1]%2==1:
        return 'NO'
    return str(ans)

print(fairRations([4,5,6,7]))
print(fairRations([2, 3, 4, 5, 6]))
print(fairRations([1,2]))