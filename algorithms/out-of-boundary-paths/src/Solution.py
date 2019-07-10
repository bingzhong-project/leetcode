class Solution:
    def findPaths(self, m: 'int', n: 'int', N: 'int', i: 'int',
                  j: 'int') -> 'int':
        def func(m, n, N, i, j, memo):
            if (i, j, N) in memo:
                return memo[(i, j, N)]
            if i < 0 or j >= n or i >= m or j < 0:
                return 1
            if N == 0:
                return 0
            left_count = func(m, n, N - 1, i - 1, j, memo)
            right_count = func(m, n, N - 1, i + 1, j, memo)
            up_count = func(m, n, N - 1, i, j - 1, memo)
            down_count = func(m, n, N - 1, i, j + 1, memo)
            total_count = left_count + right_count + up_count + down_count
            memo[(i, j, N)] = total_count
            return total_count

        res = func(m, n, N, i, j, {})
        return res % (10**9 + 7)
