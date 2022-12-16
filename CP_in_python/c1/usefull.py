#enumerate
L=[1,2,3,4,5]
for idx,val in enumerate(L):
    print (str(idx) + ' '+ str(val))

#list comprehension
squares=[x ** 2 for x in range(11)] #0 a 10
print(squares)

t=[0 for _ in range(10)] #10 itens com valor 0
print(t)

#dictionary comprehension
s1='Meus testes'
dic1={letter:0 for letter in s1}
print(dic1)

#inicializando matriz quadrada - 2 maneiras
M1=[[0]*10 for _ in range(10)]
print(M1)
M2=[[0 for j in range(10)] for i in range(10)]
print(M2)

#Pacotes importantes
#math
#fractions
#bisect
#heapq
#string
#colletions
#numpy

#Conteudo do livro disponivel como pacote
#pip install tryalgo
#import tryalgo
#help(tryalgo)
#help(tryalgo.arithm)

#Input 
# Lendo de arquivo e escrevendo na saida
#python prog.py < test.in > test.out
# para escrever na tela ao mesmo tempo
#python prog.py < test.in | tee test.out

#lendo 2 variaveis e ja convertendo a int
#import sys
#v1,v2=map(int,sys.stdin.readline().split())

#se forem apenas strings..
#v1,v2=input().split()

#Output
testCase=1
ans=11.213455
print(f'Case: #{testCase}: {ans:.2f}') #imprimir como float e 2 cadas decimais

#Complexidade
#Tamanho entrada | complexidade aceitável
# 1000000 | O(n)
# 100000  | O(n log n)
# 1000    | O(n^2)

#DS and how to quick use it in python
# Stacks -> use a list, having append as push and accessing/deleting last elem as pop
# Dicionarios -> built in no python
# Queue -> há 2 implementacoes: Queue (suporta multiprocessamento - nao recomendado para CP) / deque (double ended queue - recomendado - biblioteca collections)
   # metodos: append(elem), popleft(), appendleft(elem), pop()
# Priority queues and heaps -> modulo heapq
    # metodos: converter array A em heap (heapify(A)), add elem: (heappush(heap, elem)) e extrair elem min: (heappop(heap))
    # No material do livro também há uma implementacao do heap, já que por padrao o heapq nao permite alterar um dado
# Union-find: permite armazenar uma particao do conjunto universo. 
    # Metodos:find (se find(u)==find(v), comparamos se ambos sao parte do mesmo conjunto). union(u,v), combina os 2 conjuntos
    # No material do livro há a implementacao possível, utilizada para verificar se grafos sao conectados.

# Tecnicas
# 1.Comparacao - sao comparadas de maneira lexicografica, sendo 1o elemento, seguido do 2o elemento, etc
def majority(L):
    count={}
    for word in L:
        if word in count: count[word]+=1
        else: count[word]=1
    val_max,arg_max=min((-count[word],word) for word in count) # equivalente a expressao abaixo
    # val_max2,arg_max2=max((count[word],word) for word in count)
    return arg_max
print(majority("ThiagooTT"))

# 2. Sorting
#O(n log n)

# 3. Sweep Line - TBS (To be studied)

# 4. Greedy - TBS

# 5. Dynamic Programming
#tip: adicionando o decorador @lru_cache(maxsize=None) (da biblioteca functools), evitamos a explosao combinatorial de chamadas. 
# Ou seja, transformamos automaticamente uma implementacao recursiva em DP
#Exemplo abaixo para fibo
from functools import lru_cache
@lru_cache(maxsize=None) 
def fibo_naive(n): 
    if n<=1: return n
    return fibo_naive(n - 1) + fibo_naive(n - 2)

print(fibo_naive(10))

# 6. Encoding of Sets by Integers - TBS

# 7. Binary search