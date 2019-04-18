class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        pos = []
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                pos[table[s[i]]] = None
            else:
                pos.append(i)
                table[s[i]] = len(pos) - 1
        for p in pos:
            if p is not None:
                return p
        return -1
