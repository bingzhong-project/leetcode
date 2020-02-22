class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        array = []
        count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                array.append(count)
                count = 1
        array.append(count)
        res = 0
        for i in range(len(array) - 1):
            res += min(array[i], array[i + 1])

        return res
