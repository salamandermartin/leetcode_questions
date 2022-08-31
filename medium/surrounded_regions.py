class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != 'O':
                return
            
            if board[r][c] == 'O':
                board[r][c] = '.'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
                
        def border_dfs():
            for i in range(len(board[0])):
                dfs(0, i)
                dfs(len(board) - 1, i)
                
            for i in range(len(board)):
                dfs(i, 0)
                dfs(i, len(board[0]) - 1)
                
                
        border_dfs()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                    
            
            
            
            