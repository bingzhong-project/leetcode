class Solution:
    def numSquares(self, n):
        """
        TLE

        :type n: int
        :rtype: int
        """
        dp = [2**31 for _ in range(n + 1)]
        squares = list()
        for i in range(1, n + 1):
            squares.append(i * i)
            if i in squares:
                dp[i] = 1
            else:
                for s in squares:
                    if s > i:
                        break
                    dp[i] = min(dp[i], dp[s] + dp[i - s], dp[i - 1] + 1)

        return dp[-1]
