import collections


class Solution:
    def longestSubstring(self, s: 'str', k: 'int') -> 'int':
        def longest(string, k):
            if len(string) < k:
                return 0
            char_counter = collections.Counter(string)
            for c in char_counter:
                if char_counter[c] < k:
                    return max(longest(sub, k) for sub in string.split(c))
            return len(string)

        return longest(s, k)
