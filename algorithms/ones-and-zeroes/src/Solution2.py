class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """TLE
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            zeros = sum(c == '0' for c in s)
            ones = len(s) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[-1][-1]
