def solve(n):
    nI=int(n)
    ans=[]
    cnt=0
    mul=1
    while nI:
        if nI%10>0:
            ans.append((nI%10)*mul)
            cnt+=1
        mul*=10
        nI//=10            
    print(cnt)
    for i in ans:
        print(' '+str(i), end='')
    print()

for _ in range(int(input())):
    n=input()
    solve(n)