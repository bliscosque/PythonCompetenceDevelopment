L=[1,2,3,4]
print(list(map(lambda x:x*3,L)))
print(list(filter(lambda x:x<3,L)))

from functools import reduce
total=reduce(lambda acc,el:acc+el,L,0) 
print(total)