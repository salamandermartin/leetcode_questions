class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount = 0
        count = 0
        
        def counter(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            
            grid[r][c] = None
            return 1 + counter(r, c + 1) + counter(r + 1, c) + counter(r , c - 1) + counter(r - 1, c)
                
                
                
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = counter(i, j)
                    if count > maxCount:
                        maxCount = count
                
        return maxCount