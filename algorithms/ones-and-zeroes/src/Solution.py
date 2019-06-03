import collections


class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """TLE
        """

        def func(counter, m, n, cache):
            if (m, n) in cache:
                return cache[(m, n)]
            res = 0
            for i in range(len(counter)):
                ans = 0
                m -= counter[i][0]
                n -= counter[i][1]
                if m >= 0 and n >= 0:
                    ans = func(counter[i + 1:], m, n, cache) + 1
                m += counter[i][0]
                n += counter[i][1]
                res = max(res, ans)
            cache[(m, n)] = res
            return res

        counter = [collections.Counter() for _ in range(len(strs))]
        strs.sort(key=lambda s: len(s))
        for i in range(len(strs)):
            for s in strs[i]:
                if s == '0':
                    counter[i][0] += 1
                else:
                    counter[i][1] += 1
        cache = collections.Counter()
        res = func(counter, m, n, cache)

        return res
