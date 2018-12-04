class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_length = 0
        dp = [[0 for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num = int(matrix[i][j])
                if num == 0 or i == 0 or j == 0:
                    dp[i][j] = num
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])
        return max_length**2
