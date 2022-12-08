def LPS(s,idx1,idx2):
    if idx1>idx2: return 0 
    elif idx1==idx2: return 1 #meio da string... esse elem é comum
    elif s[idx1]==s[idx2]: #char iguais
        return 2+LPS(s,idx1+1,idx2-1)
    else: #char is not matching
        op1=LPS(s,idx1, idx2-1)
        op2=LPS(s,idx1+1, idx2)
        return max(op1, op2)

print(LPS('ELRMENMET',0,8))