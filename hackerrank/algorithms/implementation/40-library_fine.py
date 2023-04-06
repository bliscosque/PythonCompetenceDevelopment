def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        return 10000
    if y1==y2 and m1>m2:
        return 500*(m1-m2)
    if y1==y2 and m1==m2 and d1>d2:
        return 15*(d1-d2)
    return 0

print(libraryFine(14,7,2018,5,7,2018))
print(libraryFine(9,6,2015,6,6,2015))
print(libraryFine(2,7,1014,1,1,1015))