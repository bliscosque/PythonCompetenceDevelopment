nDays=int(input("Quantos dias? "))
total=0
temp=[]
for i in range(0,nDays):
    nextDay=int(input("Temperatura no dia " + str(i+1) + ": "))
    temp.append(nextDay)
    total+=nextDay

avg=round(total/nDays,2)
print("Temperatura media = " + str(avg))
above=0
for i in temp:
    if i>avg: above+=1

print(str(above) + " dias maiores que a media")