def calc(n0,n1):
    a=[n0,n1]
    a.sort()
    if a[0]==1 and a[1]==2: return 100
    if a[0]==a[1]: return 90+a[0]
    else: return a[1]*10+a[0]


s0,s1,r0,r1=[int(x) for x in input().split()]
while s0!=0 and s1!=0 and r0!=0 and r1!=0:
    p1=calc(s0,s1)
    p2=calc(r0,r1)
    if p1==p2:
        print('Tie.')
    elif p1>p2:
        print('Player 1 wins.')
    else:
        print('Player 2 wins.')
    s0,s1,r0,r1=[int(x) for x in input().split()]
