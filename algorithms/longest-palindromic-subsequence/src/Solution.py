class Solution:
    def longestPalindromeSubseq(self, s: 'str') -> 'int':
        """TLE
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + max(max(row) for row in dp[i + 1:][:j])
                else:
                    dp[i][j] = max(dp[i])
        return max(max(row) for row in dp)
