import math
def jumpingOnClouds(c):
    def jumpingOnClouds_int(c,i=0):
        if i>=len(c)-1: return 0
        if c[i]==1: return math.inf
        op1=1+jumpingOnClouds_int(c,i+1)
        op2=1+jumpingOnClouds_int(c,i+2)
        return min(op1,op2)
    return jumpingOnClouds_int(c)

print(jumpingOnClouds([0,1,0,0,0,1,0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0,0,1,0]))