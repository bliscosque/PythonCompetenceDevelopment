for _ in range(int(input())):
    line=input()
    if '+' in line:
        n1,n2=line.split('+')
        print(int(n1)+int(n2))
    else:
        print('skipped')