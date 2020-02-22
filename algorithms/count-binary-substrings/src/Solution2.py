class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        res = 0
        prev = 0
        count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                res += min(prev, count)
                prev = count
                count = 1
        res += min(prev, count)

        return res
