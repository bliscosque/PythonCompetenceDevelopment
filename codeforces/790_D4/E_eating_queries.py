def solve():
    n,q=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]

    a.sort(reverse=True)
    p_sum=[a[0]]
    for i in range(1,n):
        p_sum.append(p_sum[i-1]+a[i])

    #print(max(a))
    # db=[-1]
    # db.append(max(a)) #1a posicao: 1 elemento
    # for i in range(1,n):
    #     n_max=0
    #     for j in range(0,n-i):
    #         sum=0
    #         for k in range(j,j+i+1):
    #             sum+=a[k]
    #         n_max=max(n_max,sum)
    #     db.append(n_max)
    #print(db)

    # for _ in range(q):
    #     x=int(input())
    #     ok=False
    #     for i in range(len(db)):
    #         if db[i]>=x:
    #             print(i)
    #             ok=True
    #             break
    #     if not ok: print(-1)
    # print(p_sum)

    for _ in range(q):
        x=int(input())
        # print(f'x: {x}')
        ok=False
        for i in range(len(p_sum)):
            if p_sum[i]>=x:
                print(i+1)
                ok=True
                break
        if not ok: print(-1)

for _ in range(int(input())):
    solve()