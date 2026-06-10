class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m,n = len(board),len(board[0])

        def dfs(i,j):
            if not (0<=i<m) or  not (0<=j<n) or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0,i)
        for i in range(1,m):
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for i in range(n-2,-1,-1):
            if board[m-1][i] == 'O':
                dfs(m-1,i)
        for i in range(m-2,-2,-1):
            if board[i][0] == 'O':
                dfs(i,0)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
