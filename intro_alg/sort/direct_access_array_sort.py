def direct_access_sort(A):
    #Assume itens inteiros, distintos, nao negativos, no range de 0..u-1
    u=1+max([x for x in A]) #encontra max
    D=[None]*u #direct access array
    for x in A:
        D[x]=x
    i=0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i+=1

A=[5,2,7,0,4]
direct_access_sort(A)
print(A)