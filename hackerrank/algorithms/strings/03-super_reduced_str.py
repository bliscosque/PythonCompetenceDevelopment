def superReducedString(s):
    has_rep=True
    while has_rep:
        hr_int=False
        #print(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                hr_int=True
                s=s[0:i]+s[i+2:]
                break
        if not hr_int: has_rep=False
    if len(s)>0: return s
    return 'Empty String'

print(superReducedString('aab'))
print(superReducedString('abba'))
print(superReducedString('aaabccddd'))
print(superReducedString('aa'))