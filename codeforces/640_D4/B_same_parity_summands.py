def solve():
    n,k=[int(i) for i in input().split()]
    if (n%2==1): #soma impar
        if n>=k and k%2==1: # qnt impar de elementos... se for par, nao terá solucao
            print ("YES1")
        else:
            print("NO1")
    else: # soma par
        if n>=k/2: # qnt par de elementos
            print ("YES2")
            ans='2 '*(n//k)
            ans+=str(n-(2*n//k))
            print(ans)
        elif n>=k and k%2==1: # soma par nao funciona... testando soma impar (valido apenas qnt// impar de elem)
            print ("YES3")
        else:
            print("NO2")

for _ in range(int(input())):
    solve()