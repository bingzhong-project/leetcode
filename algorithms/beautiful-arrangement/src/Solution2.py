class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def dfs(i, numbers, dp={}):
            if len(numbers) == 1:
                return 1
            key = (i, numbers)
            if key in dp:
                return dp[key]
            total = 0
            for j, number in enumerate(numbers):
                if number % i == 0 or i % number == 0:
                    total += dfs(i - 1, numbers[:j] + numbers[j + 1:], dp)
            dp[(i, numbers)] = total
            return total

        return dfs(N, tuple([i for i in range(1, N + 1)]))
