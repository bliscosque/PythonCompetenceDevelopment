import random
c=random.randint(1,10) #inclui 1 e 10
c=random.random() #gera float de 0 a 1, nao inclui 1
c=random.random()*10 #gera float de 0 a 10, nao inclui 10
lst=[1,2,3,4,5]
print(random.choice(lst))#elem aleatorio da lista
random.shuffle(lst) # "embaralha" a lista
print(lst)
print(c)