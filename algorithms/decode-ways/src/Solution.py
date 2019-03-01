class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if len(s) == 0:
            return 1

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            num = int(s[i - 2:i])
            if num <= 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
