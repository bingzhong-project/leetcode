class Solution:
    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
        table = {}
        for s in ransomNote:
            table[s] = table[s] + 1 if s in table else 1
        for s in magazine:
            if s in table:
                table[s] -= 1
                if table[s] == 0:
                    del table[s]
        return len(table) == 0
