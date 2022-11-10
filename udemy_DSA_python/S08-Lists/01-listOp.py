shoppingList=['milk', 'cheese', 'butter']
print(shoppingList[0]) # Access / Se tentar acessar fora do range: IndexError
print(shoppingList[-1]) # Ultimo elem
print('cheese' in shoppingList) # verifica existencia

print("###")
for i in shoppingList: print(i)
print("###")

myList=[1,2,3,4,5,6,7]
print(myList)
myList[2]=33 #update elem
print(myList)

# Inserindo elem
print("###")
myList.insert(0,11) # no inicio (idx=0)
print(myList)
myList.append(99) # no final
print(myList)
newList=[100,101,102]
myList.extend(newList) # adiciona outra lista no final da lista atual
print(myList)

#Slice
print("###")
myList=['a','b','c','d','e','f']
print(myList[0:2]) # do 0 (incluido) ao 2 (nao incluido)
myList[0:2] = ['x','y'] # atualizando usando slice
print(myList)

# delete
print("###")
print(myList.pop(1)) # delete (e retorna) elem pos 1
print(myList.pop()) # delete (e retorna) last elem
del myList[2] # deleta elem pos 2. Pode usar slice
print(myList)
myList.remove('e') # busca e apaga um elemento
print(myList)

# Searching
print("###")
myList=[i for i in range(10)]
print(myList)
if 5 in myList: print(myList.index(5))
else: print ('nao existe')

# Mais operacoes e funcoes
a=[1,2,3]
b=[4,5,6]
c=a+b # + -> concatenate list
print(c)
a=[0]
a=a*4 #repetir 4 vezes
print(a)
print(len(c)) # num de elem
print(max(c)) # maior elem da lista
print(min(c)) # menor elem da lista
print(sum(c)) # soma dos elem da lista
print(sum(c)/len(c)) # media

# Converter str para lista 
a='spam'
b=list(a) # converte str para lista de char
print(b)
c='sou uma str'
d=c.split() # split usando delimitador=' '
print(d)
print('-'.join(d)) #ao contrario, usando '-' como delimitador

# Copiando lista 
copyList=d[:] # se quero copia (e nao apenas ponteiro) usar o slice