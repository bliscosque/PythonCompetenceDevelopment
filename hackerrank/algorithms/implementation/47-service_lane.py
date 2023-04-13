def serviceLane(n, cases):
    ans=[]
    for case in cases:
        i,j=case
        ans.append(min(n[i:j+1]))
    return ans

#print(serviceLane([2,3,2,1],[[1,2],[2,4]]))
print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3],[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))