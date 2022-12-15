class nQueens:
    def __init__(self,n) -> None:
        self.n=n
        self.chess_table=[[0 for i in range(n)] for j in range (n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j]==1:
                    print(" Q ",end='')
                else:
                    print(" - ",end='')
            print()

    def is_place_safe(self,row,col):
        #horizontally
        for i in range(self.n):
            if self.chess_table[row][i]==1: return False
        j=col
        for i in range(row,-1,-1):
            if i<0: break
            if self.chess_table[i][j]==1: return False
            j-=1
        j=col
        for i in range(row,self.n):
            if i<0: break
            if self.chess_table[i][j]==1: return False
            j-=1
        return True

    def solve(self,col):
        if col==self.n: return True
        for row in range(self.n):
            if self.is_place_safe(row,col): 
                self.chess_table[row][col]=1
                if self.solve(col+1): return True
                self.chess_table[row][col]=0
        return False
    def solve_nQueens(self):
        if self.solve(0): self.print_queens()
        else: print("No solutions")

queens=nQueens(4)
queens.solve_nQueens()
queens=nQueens(3)
queens.solve_nQueens()