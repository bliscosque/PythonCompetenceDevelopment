def circularArrayRotation(a, k, queries):
    n=len(a)
    if k>=n: k=k%n
    n_a=a[n-k:]+a[:n-k]
    print(n_a)
    ans=[n_a[i] for i in queries]
    return ans

print(circularArrayRotation([3,4,5],4,[1,2]))
#print(circularArrayRotation([1,2,3],2,[0,1,2]))
