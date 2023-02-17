from itertools import permutations

def AtoR(A):
    ans=""
    m = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',\
         50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    A = int(A)
    for value, roman in m.items():
        while A >= value:
            ans+=roman
            A -= value
    return ans

dec2Rom={}
rom2Dec={}
for i in range(1,101):
    dec2Rom[i]=AtoR(i)
    rom2Dec[dec2Rom[i]]=i
r=input().rstrip()
mi=rom2Dec[r]
for perm in permutations(r):
    p=''.join(perm)
    if p in rom2Dec:
        mi=min(mi,rom2Dec[p])
print(dec2Rom[mi])