from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        
        def counter(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1":
                return
            
            # if (r, c) in seen:
            #     return
            
            grid[r][c] = None
            counter(r, c + 1)
            counter(r + 1, c)
            counter(r, c - 1)
            counter(r - 1, c)
                
                
                
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    counter(i, j)
                
        return count