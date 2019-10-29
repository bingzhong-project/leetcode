class Solution:
    def numFactoredBinaryTrees(self, A: list) -> int:
        def func(num, factor_map, memo):
            if num in memo:
                return memo[num]
            if num not in factor_map:
                memo[num] = 0
                return 0
            factor1, factor2 = factor_map[num]
            left_sum = func(factor1, factor_map, memo)
            right_sum = func(factor2, factor_map, memo)
            cur = left_sum + right_sum + 1

            cur = cur if factor1 == factor2 else cur * 2
            memo[num] = cur
            return cur

        factor_map = {}
        for i in range(len(A)):
            for j in range(len(A)):
                factor_map[A[i] * A[j]] = (A[i], A[j])

        res = 0
        memo = {}
        for num in factor_map.keys():
            if num in set(A):
                res += func(num, factor_map, memo)

        return res + len(A)
