def quicksort(A,l,r):
    if l<r:
        q=partition(A,l,r)
        quicksort(A, l, q-1)
        quicksort(A, q+1, r)
    
def partition(A,l,r): # A[l..r]
    pivot=A[r]
    i=l-1 # i=put next elem at...
    for j in range(l,r): # j=elem to be checked. swap it with i if <= pivot
        if A[j]<=pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1] # next elem will have pivot
    return i+1

A=[5,13,2,25,7,17,20,8,4]
quicksort(A,0,len(A)-1)
print(A)