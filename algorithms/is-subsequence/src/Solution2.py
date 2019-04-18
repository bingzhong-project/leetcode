class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if len(s) == 0:
            return True
        pos = 0
        for string in t:
            if string == s[pos]:
                pos += 1
                if pos == len(s):
                    return True
        return False
