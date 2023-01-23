n=int(input())
a=[int(i) for i in input().split()]
ans=[1]*n
for i,idx in enumerate(a):
    ans[idx+1]=i+2
for i in ans:
    print(i, end=' ')
print()