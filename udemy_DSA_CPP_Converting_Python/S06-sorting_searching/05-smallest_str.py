#given a list of strings a1,a2,...,an. Return all the strings concatenated such that the result str would be lexicographically smallest.

#comparar sempre as strings "2 a 2", ou seja, alterar o metodo de comparacao utilizado

import functools
def compare(a,b):
    if a+b<b+a: return -1
    else: return 1


input1=['c','cb','cba'] #cbacbc
input2=['a','ab','aba'] #aabaab

input1.sort(key=functools.cmp_to_key(compare))
print(''.join(input1))
#print(sorted(input1,key=compare))
input2.sort(key=functools.cmp_to_key(compare))
print(''.join(input2))