myDict=dict()
print(myDict)

secondDict={}
print(secondDict)

engToSpanish={"one": "uno", "two": "dos", "three": "tres"}
print(engToSpanish)
print(engToSpanish["two"])

engToSpanish['four']='cuatro' #novo elem, key nao existe
engToSpanish['one']='un' #altera elem, key já existe
print(engToSpanish)

for key in engToSpanish:
    print(key,engToSpanish[key])

print(engToSpanish.pop('one')) #remove (e retorna valor)
print(engToSpanish)
print(engToSpanish.popitem()) #remove um item aleatorio
del engToSpanish['three']
print(engToSpanish)

newDict={}.fromkeys([1,2,3],0)
print(newDict)
print(newDict.get(1))
print(newDict.get(99)) #nao existe, retorna None
print(newDict.get(99,-1)) #nao existe, retorna -1

print(newDict.items()) #retorna pares de chave,valor
print(newDict.keys()) #apenas chaves
print(newDict.values()) #apenas valores

newDict.setdefault(4, 'added')
print(newDict)
newDict.setdefault(4, 'new value') #nao substitui

print(4 in newDict)
print(99 in newDict)

bDict={1:True, 2:True}
print(all(bDict)) # True, ja que TODOS os valores sao True
print(any(bDict)) # True, já que QUALQUER valor é True

nDict={'c':3, 'b':1, 'z':99}
print(sorted(nDict))
print(sorted(nDict, reverse=True))