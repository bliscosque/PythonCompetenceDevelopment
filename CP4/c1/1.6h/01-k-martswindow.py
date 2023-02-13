year=2018
month=3 #considerando 0 a 11
sYear=int(input())
flag=False
while year<=sYear:
    if year==sYear: 
        flag=True
        break
    month+=26
    year+=(month//12)
    month%=12
print("yes" if flag==True else "no")