def findMinOperation(s1, s2, idx1, idx2):
    if idx1==len(s1): #reach end of s1
        return len(s2)-idx2
    if idx2==len(s2): #reach end of s2
        return len(s1)-idx1
    if s1[idx1]==s2[idx2]: return findMinOperation(s1,s2,idx1+1,idx2+1) # char sao iguais
    else:
        delepeOpt=1+findMinOperation(s1,s2,idx1,idx2+1)
        insertOpt=1+findMinOperation(s1,s2,idx1+1,idx2)
        replaceOpt=1+findMinOperation(s1,s2,idx1+1,idx2+1)
        return min(delepeOpt, insertOpt, replaceOpt)

print(findMinOperation('catch', 'carch',0,0))
print(findMinOperation('table', 'tbrles',0,0))