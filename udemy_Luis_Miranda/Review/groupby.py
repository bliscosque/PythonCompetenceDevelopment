from itertools import groupby

L=[('Thiago','item1'),('Thiago','item2'),('Joao','item3'),('Thiago','item4')]
key_fc=lambda x:x[0]

for k,group in groupby(L,key_fc):
    print(k + " :", list(group))

print(list(groupby(L,key_fc)))