numbers=[1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)
name='Thiago'
list_chars=[l for l in name]
print(list_chars)

numbers=[1,2,3,4,10]
squared=[n**2 for n in numbers]
print(squared)
even=[n for n in numbers if n%2==0]
print(even)

import random
names=["n1","n2","n3"]
names_numb={name:random.randint(1,100) for name in names}
print(names_numb)
best_40={name:val for (name,val) in names_numb.items() if val >=40}
print(best_40)