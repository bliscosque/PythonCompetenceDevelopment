from itertools import zip_longest

l1=['Salvador', 'Ubatuba','Belo Horizonte']
l2=['BA','SP','MG','RJ']

def zippest (l1,l2):
    new_list=[(l1[i],l2[i]) for i in range(min(len(l1),len(l2)))]
    return new_list

print(zippest(l1,l2))
print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2)))
