def solve(n, dct):
    if n in dct: return dct[n]
    x=[n]
    while True:
        x.append(len(str(x[-1])))
        if x[-1] in dct: 
            dct[n]=len(x)-1+dct[x[-1]]
            return dct[n]
        #print(x) 
        if x[-1]==x[-2]:
            dct[n]=len(x)-1
            return dct[n]


n=input()
dct={}
dct[1]=1
while n!='END':
    n=int(n)
    print(solve(n,dct))
    n=input()