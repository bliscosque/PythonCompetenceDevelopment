def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def max_heapify(A,n,i):
    l=left(i)
    r=right(i)
    maior=i
    if l<n and A[l]>A[i]:
        maior=l
    if r<n and A[r]>A[maior]:
        maior=r
    if (maior!=i):
        A[i],A[maior] = A[maior],A[i]
        max_heapify(A, n, maior)

def build_max_heap(A,n):
    for i in range(n//2,-1,-1):
        max_heapify(A,n,i)

def heapsort(A):
    n=len(A)
    build_max_heap(A,n)
    for i in range(len(A)-1,0,-1):
        A[i],A[0]=A[0],A[i]
        max_heapify(A, i, 0)

#A=[16,4,10,14,7,9,3,2,8,1]
#max_heapify(A, 1)
#A=[4,1,3,2,16,9,10,14,8,7]
#build_max_heap(A)
A=[16,14,10,8,7,9,3,2,4,1]
heapsort(A)
print(A)