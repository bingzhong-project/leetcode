class Solution:
    def numFactoredBinaryTrees(self, A: list) -> int:
        def func(num, factor_map, memo):
            if num in memo:
                return memo[num]
            if num not in factor_map:
                factor_map[num] = 0
                return 0
            factor1, factor2 = factor_map[num]

        factor_map = {}
        for i in range(A):
            for j in range(A):
                factor_map[A[i] * A[j]] = (A[i], A[j])
