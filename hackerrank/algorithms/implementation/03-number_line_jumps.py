def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        if x1==x2: return 'YES'
        return 'NO'
    t=(x2-x1)/(v1-v2)
    if t>=0 and t.is_integer():
        return 'YES'
    return 'NO'
    

print(kangaroo(0,3,4,2)) #YES
print(kangaroo(0,2,5,3)) #NO
print(kangaroo(43, 2, 70, 2)) #NO