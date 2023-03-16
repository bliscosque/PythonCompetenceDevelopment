def isSafe(mat,i,j,no):
    for k in range(9):
        if mat[k][j]==no or mat[i][k]==no: return False
    #check subgrid
    sx=(i//3)*3
    sy=(j//3)*3
    for x in range(sx,sx+3):
        for y in range(sy,sy+3):
            if mat[x][y]==no: return False
    return True

def solveSudoku(mat,i=0,j=0,n=9):
    if i==n: #solution
        for i in range(n):
            for j in range(n):
                print(mat[i][j], end=' ')
            print()
        return True
    if j==n:
        return solveSudoku(mat,i+1,0)
    if mat[i][j]!=0: # pre-filled cell
        return solveSudoku(mat,i,j+1)
    #try all possibilities
    for no in range(1,n+1):
        if isSafe(mat,i,j,no):
            mat[i][j]=no
            solveProblem=solveSudoku(mat,i,j+1)
            if solveProblem: return True
    #no option works... backtracking
    mat[i][j]=0
    return False
    

mat=[
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
]
if not solveSudoku(mat):
    print("No solution")