# Given two seq, find the len of longest subs which is common to both.

def lcs(A,B):
    a,b=len(A),len(B)
    x=[[0]*(b+1) for _ in range (a+1)]
    for i in reversed(range(a)):
        for j in reversed(range(b)):
            if A[i]==B[j]:
                x[i][j]=x[i+1][j+1]+1
            else:
                x[i][j]=max(x[i+1][j],x[i][j+1])
    return x[0][0]

def lcs_rec(A,B,i,j, dp={}):
    if (i,j) in dp: return dp[(i,j)]
    if i==len(A) or j==len(B): return 0
    if A[i]==B[i]: 
        dp[(i,j)]=1+lcs_rec(A,B,i+1,j+1) #match... 1+ and check rest of str
    else:
        op1=lcs_rec(A,B,i+1,j)
        op2=lcs_rec(A,B,i,j+1)
        dp[(i,j)]=max(op1,op2)
    return dp[(i,j)]

s1="ABCD"
s2="ABEDG"
print(lcs(s1,s2)) # 3 (ABD)
print(lcs_rec(s1,s2,0,0)) 