class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, column = len(grid), len(grid[-1])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(column):
                if i == 0 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0 and i > 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif j > 0 and i > 0:
                    dp[i][j] = min(dp[i][j - 1] + grid[i][j],
                                   dp[i - 1][j] + grid[i][j])
        return dp[-1][-1]
