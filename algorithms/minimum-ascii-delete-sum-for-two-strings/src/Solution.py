class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(
                        s2[j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        sum_ascii = 0
        for s in s1:
            sum_ascii += ord(s)
        for s in s2:
            sum_ascii += ord(s)

        return sum_ascii - dp[-1][-1]
