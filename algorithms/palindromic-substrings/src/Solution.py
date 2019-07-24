class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        res = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if i == j:
                    dp[i][j] = True
                elif i - j == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif i - j > 1 and s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                if dp[i][j]:
                    res += 1
        return res
