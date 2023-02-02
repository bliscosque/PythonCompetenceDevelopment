# varios lotes, cada um com x unidades. Quero comprar exatamente soma k, sendo lotes adjacentes. Quais as opções?
# Opc1: usando partial sum -> O(n^2)
# Opc2: usar partial sum e, para cada numero, buscar o segundo (complemento) usando binary search -> O(nlogn)
# Opc3: usando sliding window

def housing(A,k):
    n=len(A)
    s=0
    j=0
    ans=[]
    for i in range(n):
        s+=A[i]
        while s>k:
            s-=A[j]
            j+=1
        if s==k: ans.append((j,i))
        
    return ans

plots=[1,3,2,1,4,1,3,2,1,1,2]
k=8 #(2,5), (4,6), (5,9) -> sendo (pos_inicial, pos_final)
print(housing(plots,k))