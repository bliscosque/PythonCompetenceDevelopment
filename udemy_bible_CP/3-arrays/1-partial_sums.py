
def buildPartialSums(a):
    s=[a[0]]
    for i in range(1,len(a)):
        s.append(s[i-1]+a[i])
    print('s:', s)
    return s

def query(l,r,s):
    if l==0: return s[r]
    return s[r]-s[l-1]

a=[7, -2, 3, 9, -11, 5, 1, -3]
s=buildPartialSums(a)
print(query(1,5,s))
print(query(4,7,s))