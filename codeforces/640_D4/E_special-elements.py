def solve():
    n=int(input())
    nums=[int(i) for i in input().split()]
    sums=set()
    for i in range(2,n+1):
        for j in range(n-i+1):
            sum=0
            for k in range(i):
                sum+=nums[j+k]
            sums.add(sum)
    ans=0
    #print(sums)
    for num in nums:
        if num in sums: ans+=1
    print(ans)


for _ in range(int(input())):
    solve()