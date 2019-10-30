class Solution:
    def numFactoredBinaryTrees(self, A: list) -> int:
        M = 10**9 + 7
        dp = {}
        A.sort()
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                div, mod = divmod(A[i], A[j])
                if mod != 0:
                    continue
                if div not in dp:
                    continue
                dp[A[i]] = (dp[A[i]] + dp[A[j]] * dp[div]) % M
        res = 0
        for num in dp.values():
            res = (res + num) % M
        return res
