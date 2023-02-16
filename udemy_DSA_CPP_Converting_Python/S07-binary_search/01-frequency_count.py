# given sorted arr which can contain repeated elem, and an elem k, we need to find the freq of a given elem

import bisect
def lower_bound(a,key):
    s=0
    e=len(a)-1
    ans=-1
    while s<=e:
        mid=(s+e)//2
        if a[mid]==key:
            ans=mid
            e=mid-1
        elif a[mid]>key:
            e=mid-1
        else:
            s=mid+1
    return ans

def upper_bound(a,key):
    s=0
    e=len(a)-1
    ans=-1
    while s<=e:
        mid=(s+e)//2
        if a[mid]==key:
            ans=mid
            s=mid+1
        elif a[mid]>key:
            e=mid-1
        else:
            s=mid+1
    return ans

input=[0,1,1,2,3,3,3,3,3,4,5,5,5,10]
print(upper_bound(input,3)-lower_bound(input,3)+1) # 5, já q 3 aparece 5 vezes

#Usando bisect (o left retorna primeiro elemento com esse valor e o right, uma posicao depois do ultimo elemento com este valor)
print(bisect.bisect_right(input,3)-bisect.bisect_left(input,3))