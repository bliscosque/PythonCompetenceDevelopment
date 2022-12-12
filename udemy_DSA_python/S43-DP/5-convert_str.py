#Top Down
def findMinOperation(s1, s2, idx1, idx2, dpDict):
    if idx1==len(s1): #reach end of s1
        return len(s2)-idx2
    if idx2==len(s2): #reach end of s2
        return len(s1)-idx1
    if s1[idx1]==s2[idx2]: return findMinOperation(s1,s2,idx1+1,idx2+1, dpDict) # char sao iguais
    else:
        dictKey=str(idx1)+str(idx2)
        if dictKey not in dpDict:
            delepeOpt=1+findMinOperation(s1,s2,idx1,idx2+1, dpDict)
            insertOpt=1+findMinOperation(s1,s2,idx1+1,idx2, dpDict)
            replaceOpt=1+findMinOperation(s1,s2,idx1+1,idx2+1, dpDict)
            dpDict[dictKey]=min(delepeOpt, insertOpt, replaceOpt)
        return dpDict[dictKey]

print(findMinOperation('catch', 'carch',0,0, {}))
print(findMinOperation('table', 'tbrles',0,0, {}))