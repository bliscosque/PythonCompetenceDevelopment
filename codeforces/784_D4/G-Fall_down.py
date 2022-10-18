nT=int(input())
while nT>0:
    mn=input()
    mn=mn.split(' ')
    m,n=int(mn[0]),int(mn[1])
    board=[]
    for i in range(m):
        strLine=[*input()]
        board.append(strLine)
    #print(board)
    for j in range(n): #para cada coluna
        cnt=0
        for i in range(m): #para cada linha
            if board[i][j]=='.': continue
            if board[i][j]=='*': 
                board[i][j]='.'
                cnt+=1
            if board[i][j]=='o' and cnt>0:
                for i1 in range(i-1,i-(1+cnt),-1): 
                    board[i1][j]='*'
                cnt=0
        if (cnt>0):
            for i1 in range(m-1,m-1-cnt,-1): 
                board[i1][j]='*'
    for l in board:
        print(''.join(l))
    nT-=1