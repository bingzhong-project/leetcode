class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        ri = 0
        rj = 0
        rdiff = 0
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                if dp[i][j]:
                    diff = j - i
                    if diff > rdiff:
                        ri = i
                        rj = j
                        rdiff = diff
        return s[ri:rj + 1]
