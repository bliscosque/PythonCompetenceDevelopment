def countApplesAndOranges(s, t, a, b, apples, oranges):
    aA,aO=0,0
    for apple in apples:
        pos=apple+a
        if pos>=s and pos<=t: aA+=1
    for orange in oranges:
        pos=orange+b
        if pos<=t and pos>=s: aO+=1
    print(aA)
    print(aO)


countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])