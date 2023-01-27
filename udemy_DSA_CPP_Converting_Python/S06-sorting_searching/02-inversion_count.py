# fiven arr of ints, need to count # of inversions
# inversion: two elem a[i] and a[j] form an inversion if a[i]>a[j] and i<j

# op1 - brute force O(n^2)
# op2 - aplicando D&C
#   - inversoes na parte esquerda
#   - inversoes na parte direita
#   - inversoes "cross", ou seja, entre as 2 partes -> durante o "merge" do merge_sort, calculamos as inversoes

def merge(arr,s,e):
    i=s
    m=(s+e)//2
    j=m+1
    temp=[]
    cnt=0
    while i<=m and j<=e:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            cnt+=(m-i+1)
            temp.append(arr[j])
            j+=1
    #elementos restantes
    while i<=m: 
        temp.append(arr[i])
        i+=1
    while j<=e:
        temp.append(arr[j])
        j+=1
    k=0
    for idx in range(s,e+1):
        arr[idx]=temp[k]
        k+=1
    #print(arr)
    return cnt

def countInversions(A,a=0,b=None):
    if b is None: b=len(A)-1
    if a>=b: return 0
    c=(a+b)//2
    c1=countInversions(A,a,c)
    c2=countInversions(A,c+1,b)
    ci=merge(A,a,b)
    return c1+c2+ci

print(countInversions([0,5,2,3,1])) #5 (5 e (2,3,1), (2,3), (3,1))
