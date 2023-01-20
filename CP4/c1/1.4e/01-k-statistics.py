a=[int(i) for i in input().split()]
del a[0]
case=1
while True:
    print(f'Case {case}: {min(a)} {max(a)} {max(a)-min(a)}')
    case+=1
    try:
        a=[int(i) for i in input().split()]
        del a[0]
    except EOFError:
        break

    