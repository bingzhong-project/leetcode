class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        res = []
        table = {}
        for c in p:
            table[c] = table[c] + 1 if c in table else 1
        counter = len(table)
        start, end = 0, 0
        while end < len(s):
            char = s[end]
            if char in table:
                table[char] -= 1
                if table[char] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if end - start == len(p):
                    res.append(start)
                char = s[start]
                if char in table:
                    table[char] += 1
                    if table[char] > 0:
                        counter += 1
                start += 1
        return res
