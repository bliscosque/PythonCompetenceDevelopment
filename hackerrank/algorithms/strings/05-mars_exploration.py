def marsExploration(s):
    e='SOS'
    ans=0
    for i in range(len(s)):
        if s[i]!=e[i%3]:ans+=1
    return ans
    
print(marsExploration('SOSTOT'))
print(marsExploration('SOSSPSSQSSOR'))
print(marsExploration('SOSSOSSOS'))