def genSubsets(L):
    if len(L)==0:
        return [[]]
    smaller=genSubsets(L[:-1])
    extra=L[-1:]
    new=[]
    for small in smaller:
        new.append(small+extra)
    return smaller+new

sset=genSubsets([0,1,2,3])
print(sset)