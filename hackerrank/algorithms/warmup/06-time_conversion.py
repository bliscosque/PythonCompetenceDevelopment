def timeConversion(s):
    hh,mm,ssee=s.split(":")
    ss=ssee[0:2]
    ee=ssee[2:]
    ans=''
    if ee=='AM':
        if hh=='12': hh='00'
        ans=f'{hh}:{mm}:{ss}'
    if ee=='PM':
        if hh!='12': hh=int(hh)+12
        ans=f'{hh}:{mm}:{ss}'
    return ans
        


print(timeConversion("12:01:05PM"))
print(timeConversion("12:01:05PM"))
print(timeConversion("12:01:05AM"))