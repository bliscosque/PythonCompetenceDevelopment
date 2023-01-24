# Ongoing
def canPlace(p,i,j,board):
    pass

def boardPlace(p,m,n,i,j):
    if canPlace(p,i,j,board):
        board[i][j]=1 #add peca
        #atualizar valor maximo
        if i+1<=m:
            ans=boardPlace(p,m,n,i+1,j)
        else:
            if j+1<=n:
                ans=boardPlace(p,m,n,1,j+1)
            else: #terminou o tabuleiro
                return sum(board)
    board[i][j]=0
    return ans

for _ in range(int(input())):
    p,m,n=[i for i in input().split()]
    m=int(m)
    n=int(n)
    board=[[0]*(n+1)]*(m+1)
    #r=rook=torre
    #k=knight=rei
    #Q=queen=rainha
    #K=king=rei
    #quero # maximo de pecas no tabuleiro
    for j in range(1,n+1):
        boardPlace(p,m,n,1,j,board) #tenta colocar em cada posicao da primeira coluna

