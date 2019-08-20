class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def move(i, j):
            return [(i - 2, j - 1), (i - 1, j - 2), (i - 2, j + 1),
                    (i - 1, j + 2), (i + 1, j - 2), (i + 2, j - 1),
                    (i + 1, j + 2), (i + 2, j + 1)]

        def func(N: int, K: int, n: int, i: int, j: int, memo: dict):
            if i < 0 or i > N - 1 or j < 0 or j > N - 1:
                return 0
            if (n, (i, j)) in memo:
                return memo[(n, (i, j))]
            if K == n:
                return 1
            able = 0
            for (p, q) in move(i, j):
                able += func(N, K, n + 1, p, q, memo)

            memo[(n, (i, j))] = able
            return able

        return func(N, K, 0, r, c, {}) * (0.125**K)
