def repeatedString(s, n):
    n1=len(s)
    if n<=n1:
        return s[0:n].count('a')
    else:
        ans=s.count('a')*(n//n1)
        rem=n%n1
        ans+=s[0:rem].count('a')
        return ans

print(repeatedString('abc',10))
print(repeatedString('aba',10))
print(repeatedString('a',100000))