cards=input().split()
dct={}
for c in cards:
    h=c[0]
    if h in dct: dct[h]+=1
    else: dct[h]=1
print(max(dct.values()))