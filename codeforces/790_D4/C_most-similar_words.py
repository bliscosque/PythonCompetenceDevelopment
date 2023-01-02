import math
def comp(w1,w2):
    ans=0
    for i in range(len(w1)):
        ans+=max(ord(w1[i]),ord(w2[i]))-min(ord(w1[i]),ord(w2[i]))
    return ans
def solve():
    n,m=[int(i) for i in input().split()]
    words=[]
    for _ in range(n):
        words.append(input())
    ans=math.inf
    for i in range(n):
        for j in range(i+1,n):
            ans=min(ans,comp(words[i],words[j]))
    print(ans)


for _ in range(int(input())):
    solve()