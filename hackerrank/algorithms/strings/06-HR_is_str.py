def hackerrankInString(s):
    for ch in 'hackerrank':
        sp=s.find(ch)
        if sp==-1: return 'NO'
        s=s[sp+1:]
        #print(s)
    return 'YES'

print(hackerrankInString('hacckkeerrannk'))
print(hackerrankInString('hereiamstackerrank'))
print(hackerrankInString('hackerworld'))
print(hackerrankInString('hhaacckkekraraannk'))
print(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))
