def matrix_mul(A,B,C):
    for i in range(len(A)):
        for j in range (len(B[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]

A=[[1,3],[7,5]]
B=[[6,8],[4,2]]
C=[[0,0],[0,0]]
matrix_mul(A, B, C)
print(C)