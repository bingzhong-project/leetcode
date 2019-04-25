class Solution:
    def longestSubstring(self, s: 'str', k: 'int') -> 'int':
        """分治算法，TLE

        Returns:
            int: 结果
        """

        def longest(string, k):
            if len(string) < k:
                return 0
            char_counter = [0 for _ in range(26)]
            for e in string:
                char_counter[ord(e) - ord('a')] += 1
            for c in range(26):
                if char_counter[c] < k and char_counter[c] > 0:
                    for i in range(len(string)):
                        if ord(string[i]) - ord('a') == c:
                            left_len = longest(string[:i], k)
                            right_len = longest(string[i + 1:], k)
                            return max(left_len, right_len)

            return len(string)

        return longest(s, k)
