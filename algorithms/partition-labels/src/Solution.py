import collections


class Solution:
    def partitionLabels(self, S: str) -> list:
        counter = collections.Counter(S)
        left = 0
        right = 0
        res = []
        chars = set()
        zero_count = 0
        while right < len(S):
            string = S[right]
            counter[string] -= 1
            chars.add(string)
            if counter[string] == 0:
                zero_count += 1
                if zero_count == len(chars):
                    res.append(right - left + 1)
                    chars = set()
                    zero_count = 0
                    left = right + 1
            right += 1
        return res
