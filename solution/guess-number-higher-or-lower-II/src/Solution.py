class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        def dfs(dp, left, right):
            if left >= right:
                return 0
            if dp[left][right] > 0:
                return dp[left][right]
            cost = 2**31
            for i in range(left, right + 1):
                cost = min(
                    cost, i + max(dfs(dp, left, i - 1), dfs(dp, i + 1, right)))
            dp[left][right] = cost
            return cost

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dfs(dp, 1, n)
        return dp[1][n]
