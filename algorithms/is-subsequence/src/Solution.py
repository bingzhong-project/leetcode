class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        pos = 0
        for string in t:
            if pos >= len(s):
                break
            if s[pos] == string:
                dp[pos + 1] = dp[pos]
                if dp[pos + 1]:
                    pos += 1
        return dp[-1]
