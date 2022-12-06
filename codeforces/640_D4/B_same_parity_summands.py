def solve():
    n,k=[int(i) for i in input().split()]
    if (n%2==1): #soma impar
        if n>=k and (n%2==0): 
            print ("YES")
        else:
            print("NO")
    else: # soma par
        if n>=k*2 and k%2==1:
            print ("YES")
            ans='2 '*(n//k)
            ans+=str(n-(2*n//k))
            print(ans)
        elif n>=k and k%2==0: # todos elem impares
            print ("YES")
        else:
            print("NO")

for _ in range(int(input())):
    solve()