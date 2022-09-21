def baseExpansion(n,base):
    ans=[]
    while (n>0):
        ans.append(n%base)
        n=n//base
    return ans[::-1]

print(baseExpansion(20,2))
