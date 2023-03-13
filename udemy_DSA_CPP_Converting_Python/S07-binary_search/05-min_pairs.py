# given two non-empty arrays, find the pair of numbers (one from each array) whose abs difference is minimum
# print any pair with the smallest abs difference

import math
import bisect

def min_pair(a1,a2):
    diff=math.inf
    a2.sort() #since  search a2 using binary_search... must be sorted
    for x in a1:
        lb=bisect.bisect_left(a2,x)
        # left
        if lb>=1 and x-a2[lb-1]<diff:
            diff=x-a2[lb-1]
            p2=x
            p1=a2[lb-1]
        # greater/right
        if lb!=len(a2) and a2[lb]-x<diff:
            diff=a2[lb]-x
            p1=x
            p2=a2[lb]

    return (p1,p2)


a1=[-1,5,10,20,3]
a2=[26,134,135,15,17]

print(min_pair(a1,a2)) #20,17