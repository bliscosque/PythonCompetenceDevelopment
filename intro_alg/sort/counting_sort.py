def counting_sort(A):
    #assume que itens sao chaves nao negativas
    u=1+max([x for x in A])
    D=[[] for i in range(u)] #direct access array para as cadeias
    for x in A:
        D[x].append(x)
    i=0
    for chain in D:
        for x in chain:
            A[i]=x
            i+=1

A=[32,3,44,42,22]
counting_sort(A)
print(A)