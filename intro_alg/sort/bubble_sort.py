def bubble_sort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if A[j]<A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


A=[1,2,3,10,11,12]
bubble_sort(A)
print(A)
