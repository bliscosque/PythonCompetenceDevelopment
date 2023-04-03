import math
def minimumDistances(a):
    dct={}
    for idx,v in enumerate(a):
        if v in dct:
            dct[v].append(idx)
        else:
            dct[v]=[idx]
    ans=math.inf
    for el in dct.values():
        #print(el)
        if len(el)>1:
            el.sort()
            for i in range(len(el)-1):
                ans=min(ans,el[i+1]-el[i])
    if ans==math.inf: return -1
    return ans
    
print(minimumDistances([3,2,1,2,3]))
print(minimumDistances([7, 1, 3, 4, 1, 7]))