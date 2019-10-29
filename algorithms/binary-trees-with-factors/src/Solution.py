class Solution:
    def numFactoredBinaryTrees(self, A: list) -> int:
        def func(num, factor_map, memo):
            if num in memo:
                return memo[num]
            if num not in factor_map:
                memo[num] = 0
                return 0
            res = 0

            for factor1, factor2 in factor_map[num]:
                left_count = func(factor1, factor_map, memo)
                right_count = func(factor2, factor_map, memo)
                count = left_count + right_count + 1
                res += count

            memo[num] = res % (10**9 + 7)
            return memo[num]

        factor_map = {}
        for i in range(len(A)):
            for j in range(len(A)):
                key = A[i] * A[j]
                if key not in set(A):
                    continue
                if key not in factor_map:
                    factor_map[key] = set()
                factor_map[key].add((A[i], A[j]))

        res = 0
        memo = {}
        for num in A:
            res += func(num, factor_map, memo)

        return res + len(A)


if __name__ == "__main__":
    print(Solution().numFactoredBinaryTrees([2, 4, 8, 16]))
