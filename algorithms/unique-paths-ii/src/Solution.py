class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(obstacleGrid[-1]))]
              for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            row = obstacleGrid[i]
            for j in range(len(row)):
                if obstacleGrid[i][j] != 1:
                    if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                        dp[i][j] = 1
                    elif (i == 0 and j != 0 and obstacleGrid[i][j - 1] != 1
                          ) or (obstacleGrid[i - 1][j] == 1
                                and obstacleGrid[i][j - 1] != 1):
                        dp[i][j] = dp[i][j - 1]
                    elif (j == 0 and i != 0 and obstacleGrid[i - 1][j] != 1
                          ) or (obstacleGrid[i][j - 1] == 1
                                and obstacleGrid[i - 1][j] != 1):
                        dp[i][j] = dp[i - 1][j]
                    elif obstacleGrid[i][j
                                         - 1] != 1 and obstacleGrid[i -
                                                                    1][j] != 1:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]
