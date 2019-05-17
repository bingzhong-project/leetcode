class Solution:
    def characterReplacement(self, s: 'str', k: 'int') -> 'int':
        """TLE
        """
        res = 0
        for start in range(len(s)):
            end = start + 1
            remain = k
            count = 1
            while end <= len(s) - 1:
                if s[start] == s[end]:
                    count += 1
                elif remain > 0:
                    count += 1
                    remain -= 1
                else:
                    break
                end += 1
            if remain > 0:
                count += remain
                count = count if count < len(s) else len(s)
            res = max(count, res)
        return res
