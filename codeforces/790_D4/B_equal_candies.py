def solve():
    n=int(input())
    nums=[int(i) for i in input().split()]
    nmin=min(nums)
    ans=0
    for num in nums:
        ans+=(num-nmin)
    print(ans)

for _ in range(int(input())):
    solve()