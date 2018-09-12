class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        cache = dict()
        for i, now_str in enumerate(s):
            if now_str in cache:
                start = cache[now_str] + 1
            cache[now_str] = i
            res = max(res, i - start + 1)
        return res
