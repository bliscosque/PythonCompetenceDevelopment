newTuple1='a','b','c'
newTuple2=('a','b','c')
newTuple3=tuple() #tupla vazia
newTuple4=tuple('abc') #cada letra será um elemento
newTuple5=('a',) #1 elem, precisa da ,
print(newTuple1)
print(newTuple2)
print(newTuple3)
print(newTuple4)
print(newTuple5)
print(newTuple1[1])
print(newTuple1[-1])
print(newTuple1[0:1])

newTuple6=tuple('abcdef') 
for i in newTuple6:
    print(i)

print('a' in newTuple6)
print('z' in newTuple6)
print(newTuple6.index('a'))
# print(newTuple6.index('z')) #ValueError
print(newTuple6.count('a'))
print(newTuple6.count('z'))

newTuple7=tuple([1,2,3]) # converte lista para tupla
print(newTuple7)

init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)
print(result)