#given a string s, find all the permutations of the string

from itertools import permutations
perm=permutations('abc',3)
for i in list(perm): print(''.join(i))