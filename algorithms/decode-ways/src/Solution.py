class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if len(s) == 0:
            return 1
        if s[0] == '0':
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            cur = int(s[i])
            pre = int(s[i - 1])
            num = pre * 10 + cur
            if (pre == 0 and cur == 0 or (cur == 0 and num > 26)):
                return 0
            elif (pre == 0 or num > 26):
                dp[i + 1] = dp[i]
            elif (cur == 0):
                dp[i + 1] = dp[i - 1]
            else:
                dp[i + 1] = dp[i] + dp[i - 1]
        return dp[-1]
