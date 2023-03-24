def icecreamParlor(m, arr):
    s={}
    for i,v in enumerate(arr):
        if m-v in s:
            return [s[m-v]+1,i+1]
        else:
            s[v]=i

    
print(icecreamParlor(4,[1, 4, 5, 3, 2]))
print(icecreamParlor(4,[2, 2,4, 3]))