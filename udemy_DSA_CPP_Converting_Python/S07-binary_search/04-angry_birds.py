# There is a long wire along at straight line which contains N bird nests.
# There are B birds, which become angry each other once put into a nest
# You need to passign birds to nests such that minimun distance between any two buds is as large as possible.

def canPlaceBirds(b,n,nests,sep):
    birds=1
    location=nests[0]
    for i in range(1,n):
        cur_location=nests[i]
        if cur_location-location>=sep:
            birds+=1
            location=cur_location
            if birds==b: return True
    return False


def angry_birds(n,b,nests):
    nests.sort()
    s=0
    e=nests[-1]-nests[0]
    ans=-1
    while s<=e:
        mid=(s+e)//2
        canPlace=canPlaceBirds(b,n,nests,mid)
        if canPlace:
            ans=mid
            s=mid+1
        else:
            e=mid-1
    return ans


n=5
b=3
nests=[1,2,4,8,9]
print(angry_birds(n,b,nests)) #3 (pos 1,4, 9), com distancia minima de 3 (4-1=3)