class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = dict()
        res = 0
        str_len = len(s)
        cursor = 0
        while cursor < str_len:
            now_cursor = cursor
            now_str = s[cursor]
            if now_str in cache:
                new_res = len(cache)
                if res < new_res:
                    res = new_res
                cursor = cache[now_str]
                cache = dict()
            else:
                cache[now_str] = now_cursor
            cursor = cursor + 1
        new_res = len(cache)
        if res < new_res:
            res = new_res
        return res
