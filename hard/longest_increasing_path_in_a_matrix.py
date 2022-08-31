class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))] 
        
        def dfs(r, c, curr):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= curr:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]
            
            dp[r][c] = 1 + max(dfs(r + 1, c, matrix[r][c]), dfs(r - 1, c, matrix[r][c]), dfs(r, c + 1, matrix[r][c]), dfs(r, c - 1, matrix[r][c]) )
            
            return dp[r][c]
        
        
        ans = 0    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] == 0:
                    dfs(i, j, float('-inf'))
                ans = max(ans,dp[i][j])
    
        return ans