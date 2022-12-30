def solve():
    n=int(input())
    if n<=3: print(-1)
    else:
        if n%2==0:#n eh par
            for i in range(n-1,0,-2):
                print(i, end=' ')
            print(4,2, end=' ')
            for i in range(6,n+1,2):
                print(i,end=' ')
            print()
        else: #n eh impar
            for i in range(n,0,-2):
                print(i, end=' ')
            print(4,2, end=' ')
            for i in range(6,n+1,2):
                print(i,end=' ')
            print()


for _ in range(int(input())):
    solve()