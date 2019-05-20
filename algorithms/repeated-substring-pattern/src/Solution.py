class Solution:
    def repeatedSubstringPattern(self, s: 'str') -> 'bool':
        length = len(s)
        for i in range(length // 2, 0, -1):
            if length % i != 0:
                continue
            start = 0
            end = i
            sub_str = s[start:end]
            res = True
            while end < length:
                start += i
                end += i
                if s[start:end] != sub_str:
                    res = False
                    break
            if res:
                return True
        return False
