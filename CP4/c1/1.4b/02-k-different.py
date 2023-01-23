while True:
    try:
        n1,n2=[int(i) for i in input().split()]
    except EOFError:
        break
    print(abs(n1-n2))