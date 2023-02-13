a=[int(i) for i in input().split()]
a.sort()
d2=a[2]-a[1]
d1=a[1]-a[0]
if d1==d2:
    print(a[2]+d2)
elif d1>d2:
    print(a[0]+d2)
else:
    print(a[1]+d1)