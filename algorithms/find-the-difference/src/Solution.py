class Solution:
    def findTheDifference(self, s: 'str', t: 'str') -> 'str':
        diff = 0
        for c in s:
            diff ^= ord(c)
        for c in t:
            diff ^= ord(c)
        return chr(diff)
