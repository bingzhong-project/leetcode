class Solution:
    def longestPalindromeSubseq(self, s: 'str') -> 'int':
        def func(s, start, end, memo):
            if (start, end) in memo:
                return memo[(start, end)]
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                res = 2 + func(s, start + 1, end - 1, memo)
            else:
                res = max(
                    func(s, start + 1, end, memo), func(
                        s, start, end - 1, memo))
            memo[(start, end)] = res
            return res

        return func(s, 0, len(s) - 1, {})
