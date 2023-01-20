a,b,c,n=[int(i) for i in input().split()]
if a+b+c>=n and a>0 and b>0 and c>0 and n>=3:
    print('YES')
else: print('NO')