def solve():
    n=int(input())
    a=[int(i)%10 for i in input().split()]
    dct={}
    for i in a:
        if i not in dct: dct[i]=1
        else: dct[i]+=1
    for i in dct.keys():
        for j in dct.keys():
            for k in dct.keys():
                if (i+j+k)%10==3:
                    if i != j and i!=k and j!=k: # 3 diferentes
                        print("YES")
                        return
                    elif i==j and i==k and j==k: # 3 iguais
                        if dct[i]>=3:
                            print("YES")
                            return
                    elif i==j and i!=k: #i=j
                        if dct[i]>=2:
                            print("YES")
                            return
                    elif i==k and i!=j: #i=k
                        if dct[i]>=2:
                            print("YES")
                            return
                    elif j==k and i!=j: #j=k
                        if dct[j]>=2:
                            print("YES")
                            return                            
    print("NO")



for _ in range(int(input())):
    solve()