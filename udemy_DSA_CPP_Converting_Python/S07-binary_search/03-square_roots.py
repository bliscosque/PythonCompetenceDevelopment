# given ints N and P. Find the square root of N upto P places, without using lib function.

def sq_root(n,p):
    s=0
    e=n
    ans=0

    #bin search... [0..n]
    while s<=e:
        mid=(s+e)//2
        if mid*mid==n: return mid
        elif mid*mid<n:
            ans=mid
            s=mid+1
        else:
            e=mid-1
    
    #linear seach for floating part
    inc=0.1
    for place in range(1,p+1):
        while (ans*ans<=n):
            ans+=inc
        ans=ans-inc
        inc/=10
    
    return ans

print(sq_root(10,3)) # 3.162