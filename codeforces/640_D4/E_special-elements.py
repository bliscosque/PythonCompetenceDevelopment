# def solve():
#     n=int(input())
#     nums=[int(i) for i in input().split()]
#     sums=set()
#     for i in range(2,n+1):
#         for j in range(n-i+1):
#             sum=0
#             for k in range(i):
#                 sum+=nums[j+k]
#             sums.add(sum)
#     ans=0
#     #print(sums)
#     for num in nums:
#         if num in sums: ans+=1
#     print(ans)
def solve():
    n=int(input())
    nums=[int(i) for i in input().split()]
    parcialSum=[0]
    sums=set()
    for i in range(n):
        parcialSum.append(parcialSum[i]+nums[i])
    #print(parcialSum)
    for i in range(n-2+1): #o +1 é para compensar o 0 na primeira posicao
        for j in range(i+2,n+1):
            #print (i,j)
            sums.add(parcialSum[j]-parcialSum[i])
    sums.add(parcialSum[-1]) #todos os elementos 
    #print(sums)
    ans=0
    for num in nums:
        if num in sums: ans+=1
    if n==1: ans=0
    print(ans)


for _ in range(int(input())):
    solve()