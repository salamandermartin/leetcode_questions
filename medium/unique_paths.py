class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = 1
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if col + 1 > n - 1:
                    right = 0
                else:
                    right = dp[row][col + 1]
                    
                if row + 1 > m - 1:
                    down = 0
                else:
                    down = dp[row + 1][col]
                
                if dp[row][col] == 0:
                    dp[row][col] = down + right
                    
        return dp[0][0]