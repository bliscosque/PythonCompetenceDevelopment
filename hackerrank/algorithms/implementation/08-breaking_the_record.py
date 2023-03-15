def breakingRecords(scores):
    mi=ma=scores[0]
    cmi=cma=0
    for i in range(1,len(scores)):
        el=scores[i]
        if mi>el:
            mi=el
            cmi+=1
        if ma<el:
            ma=el
            cma+=1
    return [cma,cmi]

print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))