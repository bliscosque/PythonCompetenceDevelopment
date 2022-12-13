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

#Input e Output
# Lendo de arquivo e escrevendo na saida
#python prog.py < test.in > test.out
# para escrever na tela ao mesmo tempo
#python prog.py < test.in | tee test.out

#lendo 2 variaveis e ja convertendo a int
#import sys
#v1,v2=map(int,sys.stdin.readline().split())

#se forem apenas strings..
#v1,v2=input().split()

