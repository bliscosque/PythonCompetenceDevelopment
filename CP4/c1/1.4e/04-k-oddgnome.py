def solve(a):
    for i in range(1,len(a)-1):
        if (a[i-1]<a[i+1]) and (a[i]>a[i+1] or a[i-1]>a[i]):
            print(i+1)
            return
            
for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    solve(a[1:])
    