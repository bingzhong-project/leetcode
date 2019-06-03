class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """TLE
        """

        def func(strs, index, m, n, cache):
            if (index, m, n) in cache:
                return cache[(index, m, n)]
            zeros = strs[index].count('0')
            ones = len(strs[index]) - zeros
            if index == len(strs) - 1:
                cache[(index, m, n)] = 1 if zeros <= m and ones <= n else 0
                return cache[(index, m, n)]
            res = func(strs, index + 1, m, n, cache)
            if zeros <= m and ones <= n:
                res = max(
                    res, 1 + func(strs, index + 1, m - zeros, n - ones, cache))
            cache[(index, m, n)] = res
            return res

        cache = {}

        return func(strs, 0, m, n, cache)
