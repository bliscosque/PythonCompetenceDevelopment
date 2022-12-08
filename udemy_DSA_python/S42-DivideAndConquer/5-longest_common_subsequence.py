def LCS(s1,s2,idx1,idx2):
    if idx1==len(s1) or idx2==len(s2): return 0 #end of str
    if s1[idx1]==s2[idx2]:
        return 1+LCS(s1,s2,idx1+1,idx2+1) #char matches
    else:
        op1=LCS(s1,s2,idx1,idx2+1)
        op2=LCS(s1,s2,idx1+1,idx2)
        return max(op1,op2)

print(LCS('elephant', 'eretpat',0,0))