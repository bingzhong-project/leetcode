class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """TLE
        """

        def func(strs, index, m, n, cache):
            if (index, m, n) in cache:
                return cache[(index, m, n)]
            res = 0
            for i in range(index, len(strs)):
                ans = 0
                zeros = strs[i].count('0')
                ones = len(strs[i]) - zeros
                m -= zeros
                n -= ones
                if m >= 0 and n >= 0:
                    ans = func(strs, i + 1, m, n, cache) + 1
                m += zeros
                n += ones
                res = max(res, ans)
            cache[(index, m, n)] = res
            return res

        cache = {}

        return func(strs, 0, m, n, cache)
