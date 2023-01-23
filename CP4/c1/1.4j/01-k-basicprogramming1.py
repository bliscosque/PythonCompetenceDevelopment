import math, statistics
N,t=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
if t==1:
    print(7)
if t==2:
    if a[0]>a[1]:
        print("Bigger")
    elif a[0]==a[1]:
        print("Equal")
    else: 
        print("Smaller")
if t==3:
    print(statistics.median([a[0],a[1],a[2]]))
if t==4:
    print(sum(a))
if t==5:
    print(sum([i for i in a if i%2==0]))
if t==6:
    newa=[chr(i%26+ord('a')) for i in a]
    print(''.join(newa))
if t==7:
    i=0
    visited={0}
    while True:
        i=a[i]
        if i >= len(a): 
            print('Out')
            break
        elif i==len(a)-1: 
            print('Done')
            break
        if i in visited:
            print('Cyclic')
            break
        visited.add(i)
