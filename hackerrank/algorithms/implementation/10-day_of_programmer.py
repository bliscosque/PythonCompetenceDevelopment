import calendar
def dayOfProgrammer(year):
    if year>1918:
        if calendar.isleap(year):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year<=1917:
        if year%4==0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    else:
        return '26.09.1918'

print(dayOfProgrammer(2017))
print(dayOfProgrammer(2016))
print(dayOfProgrammer(1800))
print(dayOfProgrammer(1984))