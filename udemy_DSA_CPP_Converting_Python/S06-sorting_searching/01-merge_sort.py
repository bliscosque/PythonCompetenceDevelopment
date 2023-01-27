#Using MIT 6.006 rec03 implementation
def merge_sort(A,a=0,b=None):
    if b is None: b=len(A)
    if 1<b-a:
        c=(a+b+1)//2 #middle
        merge_sort(A,a,c)
        merge_sort(A,c,b)
        L,R=A[a:c],A[c:b]
        i,j=0,0
        while a<b:
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                A[a]=L[i]
                i+=1
            else:
                A[a]=R[j]
                j+=1
            a+=1

cList=[2,1,6,3,5,6,88]
merge_sort(cList, 0)
print(cList)

