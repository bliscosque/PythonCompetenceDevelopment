def merge_sort(A, a=0, b=None): #a=start, b=end
    if b is None: b=len(A)
    if 1<b-a:
        c=(a+b+1)//2 #mid
        merge_sort(A,a,c)
        merge_sort(A,c,b)
        L,R=A[a:c], A[c:b]
        merge(L,R,A,len(L),len(R),a,b)

def merge(L,R,A,i,j,a,b): #Left matrix, right matrix, original matrix
    if a<b:
        if (j<=0) or (i>0 and L[i-1] > R[j-1]):
            A[b-1]=L[i-1]
            i-=1
        else:
            A[b-1]=R[j-1]
            j-=1
        merge(L,R,A,i,j,a,b-1)

A=[5,2,4,6,1,3]
merge_sort(A)
print(A)