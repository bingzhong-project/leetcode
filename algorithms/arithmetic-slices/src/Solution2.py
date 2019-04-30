class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        dp = [0 for _ in range(len(A))]
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = 1 + dp[i - 1]
        return sum(dp)

    def numberOfArithmeticSlices2(self, A: 'List[int]') -> 'int':
        dp = 0
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res
