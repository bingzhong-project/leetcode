import collections


class Solution:
    def characterReplacement(self, s: 'str', k: 'int') -> 'int':
        if len(s) == 0:
            return 0
        res = 0
        counter = collections.defaultdict(int)
        left = 0
        right = k
        for i in range(right + 1):
            counter[s[i]] += 1
        while right < len(s):
            max_count = max(counter.values())
            length = right - left + 1
            legal = True
            if max_count < length and length - max_count > k:
                counter[s[left]] -= 1
                left += 1
                legal = False
            right += 1
            if right < len(s):
                counter[s[right]] += 1
            if legal:
                res = max(length, res)
        return res
