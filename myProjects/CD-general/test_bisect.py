# https://docs.python.org/3/library/bisect.html
import bisect
a=[1,2,3,4,5,5,5,5,10,99,0]
a.sort()
for i,el in enumerate(a):
    print(i,el)

print(bisect.bisect(a,5)) # uma posicao depois do ultimo elemento = bisect_right
print(bisect.bisect_right(a, 5)) # uma posicao depois do ultimo elemento

print(bisect.bisect_left(a, 5)) # primeiro elemento que tem este valor
