def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    sum=0
    multip=1
    for n in calorie:
        sum+=n*multip
        multip*=2
    return sum

print(marcsCakewalk([1,3,2]))
print(marcsCakewalk([7,4,9,6]))