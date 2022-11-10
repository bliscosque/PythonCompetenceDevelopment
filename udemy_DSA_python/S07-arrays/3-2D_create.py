import numpy as np

twoDimArray=np.array([[1,2,3,4],[4,3,2,1],[5,6,7,8],[8,7,6,5]])
print(twoDimArray)

# Para adicionar elementos, posso adicionar uma linha ou uma coluna nova
newTwoDArray=np.insert(twoDimArray,0,[[0,0,0,0]], axis=1) #axis=1 adiciona uma nova coluna
print(newTwoDArray)

newTwoDArray=np.insert(twoDimArray,0,[[0,0,0,0]], axis=0) #axis=0 adiciona uma nova linha
print(newTwoDArray)

newTwoDArray=np.append(twoDimArray,[[9,9,9,9]], axis=0) #adicionando ao final
print(newTwoDArray)

print(newTwoDArray[0][0])

for i in range(len(newTwoDArray)): #retorna # de linhas
    for j in range(len(newTwoDArray[0])): # retorna # de colunas
        print(newTwoDArray[i][j])
    
# Excluir uma linha ou coluna
newTwoDArray=np.delete(twoDimArray,0,axis=0) #linha
print(newTwoDArray)