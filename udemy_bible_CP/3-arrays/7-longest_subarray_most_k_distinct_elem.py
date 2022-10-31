def longest_subarr_most_k_dis(A,k):
    fr=[0]*99
    n=len(A)
    l=0
    cnt=0
    r=0
    for r in range(0,n):
        fr[A[r]]+=1
        if fr[A[r]]==1: cnt+=1 #primeira vez que el aparece
        if cnt>k: break #chegou no max dos elem
    if cnt<=k: return n #todos os elementos
    fr[A[r]]-=1
    if fr[A[r]]==0: cnt-=1
    r-=1
    ans=r
    for l in range(1,n):
        fr[A[l-1]]-=1
        if fr[A[l-1]]==0: cnt-=1
        while r < n-1:
            r+=1
            fr[A[r]]+=1
            if fr[A[r]]==1: cnt+=1
            if cnt>k: break
        if cnt<=k: return max(ans,n-l+1)
        fr[A[r]]-=1
        if fr[A[r]]==0: cnt-=1
        r-=1
        ans=max(ans,r-l+1)
        
    return ans


A=[1,5,2,1,7,2,1,5,5,7]
k=3 #max de 3 elem distintos
print(longest_subarr_most_k_dis(A,k)) #Ans=5 [2,1,7,2,1]