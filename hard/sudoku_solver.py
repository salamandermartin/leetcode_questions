class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def numRow(r, num):
            for i in board[r]:
                if i == str(num):
                    return True
                
            return False
        
        def numColumn(c, num):
            for i in range(len(board)):
                if board[i][c] == str(num):
                    return True
            return False
        
        def numBox(r, c, num):
            row = r - r % 3
            col = c - c % 3
            
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == str(num):
                        return True
            return False
        
        def validPlacement(r, c, number):
            if numRow(r, number) or numColumn(c, number) or numBox(r, c, number):
                return False
            return True
        
        def solveBoard(sudoku):
            for row in range(len(sudoku)):
                for col in range(len(sudoku[0])):
                    if sudoku[row][col] == '.':
                        for i in range(1, 10):
                            if validPlacement(row, col, i):
                                sudoku[row][col] = str(i)
                                
                                if solveBoard(sudoku):
                                    return True
                                else:
                                    board[row][col] = '.'
                        return False
            return True
        
        solveBoard(board)
        