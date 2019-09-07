class Solution:
    def findLength(self, A: list, B: list) -> int:
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        res = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
        return res
