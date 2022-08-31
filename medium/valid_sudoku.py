class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(r):
            numSet = set()
            
            for i in board[r]:
                if i == '.':
                    continue
                if i not in numSet:
                    numSet.add(i)
                else:
                    return False
            return True
                
        def checkColumn(c):
            numSet = set()
            
            for i in range(len(board)):
                if board[i][c] == '.':
                    continue
                if board[i][c] not in numSet:
                    numSet.add(board[i][c])
                else:
                    return False
            return True
        
        def checkBox(startRow, endRow, startCol, endCol):
            numSet = set()
            if endCol > len(board[0]) or endRow > len(board):
                return True
            
            for i in range(startRow, endRow + 1):
                for j in range(startCol, endCol + 1):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] not in numSet:
                        numSet.add(board[i][j])
                    else:
                        return False
            return True and checkBox(startRow + 3, endRow + 3, startCol, endCol) and checkBox(startRow, endRow, startCol + 3, endCol + 3)
        
        for i in range(len(board)):
            if not checkRow(i):
                return False
            
        for i in range(len(board[0])):
            if not checkColumn(i):
                return False
            
        if not checkBox(0, 2, 0, 2):
            return False
        
        return True
        
        