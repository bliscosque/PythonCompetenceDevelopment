def selection_sort(A,n):
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if A[min_idx]>A[j]:
                min_idx=j
        A[i],A[min_idx] = A[min_idx],A[i]

A=[5,2,4,6,1,3]
n=len(A)
selection_sort(A, n)
print(A)