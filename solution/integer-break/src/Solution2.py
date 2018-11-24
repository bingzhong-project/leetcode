class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], dp[j] * dp[i - j],
                            j * (i - j))
        return dp[-1]
