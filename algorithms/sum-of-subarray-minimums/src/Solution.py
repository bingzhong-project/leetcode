class Solution:
    def sumSubarrayMins(self, A: list) -> int:
        """TLE
        """
        MOD = 10**9 + 7
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        res = dp[0]
        for i in range(1, len(A)):
            if A[i] >= A[i - 1]:
                dp[i] = A[i] + dp[i - 1]
            else:
                j = i - 1
                while j >= 0 and A[i] <= A[j]:
                    j -= 1
                if j < 0:
                    dp[i] = A[i] * (i + 1)
                else:
                    dp[i] = A[i] * (i - j) + dp[j]
            res = (res + dp[i]) % MOD

        return res
