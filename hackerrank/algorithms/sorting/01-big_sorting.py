def bigSorting(unsorted):
    unsorted.sort(key=lambda s:(len(s),s))
    return unsorted

print(bigSorting(['1','200','150','3']))
print(bigSorting(['31415926535897932384626433832795','1','3','10','3','5']))