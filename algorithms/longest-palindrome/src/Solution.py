import collections


class Solution:
    def longestPalindrome(self, s: 'str') -> 'int':
        table = collections.defaultdict(int)
        for string in s:
            table[string] += 1
        odd = False
        res = 0
        for count in table.values():
            if count % 2 == 0:
                res += count
            else:
                odd = True
                res += (count - 1)

        if odd:
            res += 1
        return res
