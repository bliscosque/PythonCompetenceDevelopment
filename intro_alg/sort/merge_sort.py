def merge(A,s,m,e):
    nL=m-s+1
    nR=e-m
    L=A[s:s+nL]
    R=A[m+1:m+nR+1]
    i=j=0
    k=s
    while i<nL and j<nR:
        if L[i] <= R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while i<nL:
        A[k]=L[i]
        i+=1
        k+=1
    while j<nR:
        A[k]=R[j]
        j+=1
        k+=1

def merge_sort(A, s, e):
    if (s>=e):
        return
    m=int((s+e)/2)
    merge_sort(A, s, m)
    merge_sort(A, m+1, e)
    merge(A,s,m,e)

A=[5,2,4,6,1,3]
n=len(A)
merge_sort(A, 0, n-1)
print(A)