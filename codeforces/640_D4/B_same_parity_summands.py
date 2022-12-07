def solve():
    n,k=[int(i) for i in input().split()]
    if (n%2==0): #soma par
        if n/2>=k and k%2==1: # qnt impar de elementos... resposta precisa ser de pares
            print ("YES")
            ans='2 '*(k-1)
            ans+=str(n-(2*(k-1)))
            print(ans)
        #n par e k impar ->no
        elif n>=k and k%2==0:
            print ("YES")
            ans='1 '*(k-1)
            ans+=str(n-(k-1))
            print(ans)
        else:
            print("NO")
    else: # soma impar
        if n>=k and k%2==1: # n impar, k impar
            print ("YES")
            ans='1 '*(k-1)
            ans+=str(n-(k-1))
            print(ans)
        #n impar, k par -> no
        else:
            print("NO")

for _ in range(int(input())):
    solve()