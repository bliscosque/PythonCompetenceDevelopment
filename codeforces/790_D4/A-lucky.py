for _ in range(int(input())):
    n=[int(i) for i in input()]
    a1,a2=(n[0]+n[1]+n[2]),(n[3]+n[4]+n[5])
    if a1==a2: print("YES")
    else: print("NO")
