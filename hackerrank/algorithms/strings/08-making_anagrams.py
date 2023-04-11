from collections import defaultdict
def makingAnagrams(s1, s2):
    fc1=defaultdict(int)
    fc2=defaultdict(int)
    for c in s1:
        fc1[c]+=1
    for c in s2:
        fc2[c]+=1
    cntcomm=0
    for k,v in fc1.items():
        if k in fc2:
            cntcomm+=min(v,fc2[k])
    return len(s1)+len(s2)-2*cntcomm
    

print(makingAnagrams('abc','amnop'))
print(makingAnagrams('cde','abc'))