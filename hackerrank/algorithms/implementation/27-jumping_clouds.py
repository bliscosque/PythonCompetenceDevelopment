def jumpingOnClouds(c, k):
    e=100
    n=len(c)
    pos=(0+k)%n
    if c[pos]==1: e-=2
    e-=1
    #print(e,pos)
    while pos!=0:
        pos=(pos+k)%n
        e-=1
        if c[pos]==1: e-=2
    return e
    

print(jumpingOnClouds([0,0,1,0],2))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2))