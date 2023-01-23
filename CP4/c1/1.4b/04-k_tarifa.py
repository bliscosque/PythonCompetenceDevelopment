mb=int(input())
n=int(input())
s=0
for _ in range(n):
    p=int(input())
    s+=p
print(mb*(n+1)-s)