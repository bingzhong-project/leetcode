import collections


class Solution:
    def findSubstringInWraproundString(self, p: 'str') -> 'int':
        def validate(pre, cur):
            last_ord = ord(pre)
            cur_ord = ord(cur)
            if last_ord == ord('z') and cur_ord == ord('a'):
                return True
            else:
                return cur_ord == last_ord + 1

        if len(p) == 0:
            return 0
        dp = collections.Counter()
        length = 1
        dp[p[0]] = 1
        for i in range(1, len(p)):
            if validate(p[i - 1], p[i]):
                length += 1
            else:
                length = 1
            dp[p[i]] = max(dp[p[i]], length)
        return sum(dp.values())
