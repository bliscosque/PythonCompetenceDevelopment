def appendAndDelete(s, t, k):
    if s==t and k%2==0: return 'Yes'
    ls,lt=len(s),len(t)
    if k>=(ls+lt):
        return 'Yes'
    #count eq chars
    for i in range(min(ls,lt)):
        if s[i]!=t[i]: break
    #print(i)
    if k>=(ls-i)+(lt-i):
        if k%2==((ls-i)+(lt-i))%2: 
            return 'Yes'
    return 'No'

print(appendAndDelete('abc','def',6))
print(appendAndDelete('hackerhappy','hackerrank',9))
print(appendAndDelete('abc','aba',7))
print(appendAndDelete('ashley','ash',2))
print(appendAndDelete('abcd','abcdert',10)) #No