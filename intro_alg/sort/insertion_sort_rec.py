def insertion_sort(A, s, n):
    if s>=n:
        return
    key=A[s]
    j=s-1
    while (j>=0 and A[j] > key):
        A[j+1]=A[j]
        j=j-1
    A[j+1]=key
    insertion_sort(A, s+1, n)

A=[5,2,4,6,1,3]
n=len(A)
insertion_sort(A, 0, n)
print(A)