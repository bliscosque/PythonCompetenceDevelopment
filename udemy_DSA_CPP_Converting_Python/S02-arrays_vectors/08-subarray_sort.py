# given an array of size >=2, find the smallest subarray that needs to be sorted in place so that entire input arr becomes sorted
# if input already sorted, return [-1,-1], otherwise star & end index

# Approach 1: ordenar a array e verificar onde os elementos diferem -> O(NlogN)
# Approach 2: buscar elementos fora de ordem (o menor e o maior). -> O(N)
#   Um elemento fora de ordem tera o anterior e o posterior como menor que ele ou o anterior e posterior maior que ele  
#   Encontrar entao a posicao correta para esses 2 elementos fora de ordem
import math

def outOfOrder(a,i):
    x=a[i]
    if i==0: return x>a[1]
    if i==len(a)-1:
        return x<a[i-1]
    return x>a[i+1] or x<a[i-1]

def subarraySort(a):
    n=len(a)
    smallest=math.inf
    largest=-math.inf
    for i in range(n):
        if outOfOrder(a,i):
            smallest=min(smallest,a[i])
            largest=max(largest,a[i])
    if smallest==math.inf: return (-1,-1)
    
    l=0
    while smallest>=a[l]: l+=1
    
    r=n-1
    while largest<=a[r]: r-=1
    return (l,r)

a1=[1,2,3,4,5,8,5,6,9,10,11] # (5,7) -> indices de 5 a 7 [8,6,7]
print(subarraySort(a1))