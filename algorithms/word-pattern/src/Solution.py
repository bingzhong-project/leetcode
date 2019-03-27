class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        str_list = str.split(' ')
        if len(pattern) != len(str_list):
            return False

        pd = {}
        sd = {}
        for i in range(len(pattern)):
            p = pattern[i]
            s = str_list[i]
            if p not in pd and s not in sd:
                pd[p] = s
                sd[s] = p
                continue
            if p not in pd or s not in sd or pd[p] != s or sd[s] != p:
                return False
        return True
