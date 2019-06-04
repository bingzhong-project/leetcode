import collections


class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        dp = collections.Counter()
        dp[(m, n)] = 0
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            for (dm, dn), count in dp.copy().items():
                if dm - zeros >= 0 and dn - ones >= 0:
                    dp[(dm - zeros, dn - ones)] = max(
                        dp[(dm - zeros, dn - ones)], count + 1)

        return max(dp.values())
