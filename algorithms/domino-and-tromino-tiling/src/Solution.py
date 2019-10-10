class Solution:
    def numTilings(self, N: int) -> int:
        if N <= 1:
            return 1
        if N <= 2:
            return 2
        dp = [0 for _ in range(N + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)
        return dp[-1]
