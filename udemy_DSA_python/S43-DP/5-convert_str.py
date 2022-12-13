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

#Bottom Up
def findMinOperationBU(s1,s2, tmpDict):
    for i1 in range(len(s1)+1):
        dictkey=str(i1)+'0'
        tmpDict[dictkey]=i1
    for i2 in range(len(s2)+1):
        dictkey='0'+str(i2)
        tmpDict[dictkey]=i2

    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1]==s2[i2-1]:
                dictkey=str(i1)+str(i2)
                dictkey1=str(i1-1)+str(i2-1)
                tmpDict[dictkey]=tmpDict[dictkey1]
            else:
                dictkey=str(i1)+str(i2)
                dictkeyD=str(i1-1)+str(i2)
                dictkeyI=str(i1)+str(i2-1)
                dictkeyR=str(i1-1)+str(i2-1)
                tmpDict[dictkey]=1+min(tmpDict[dictkeyD], min(tmpDict[dictkeyI],tmpDict[dictkeyR]))
    dictkey=str(len(s1))+str(len(s2))
    return tmpDict[dictkey]
    
print(findMinOperation('catch', 'carch',0,0, {}))
print(findMinOperation('table', 'tbrles',0,0, {}))

print(findMinOperationBU('catch', 'carch', {}))