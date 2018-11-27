class Solution:
    def numSquares(self, n):
        """
        TLE

        :type n: int
        :rtype: int
        """
        dp = [2**31 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]
