class Solution:
    def findContentChildren(self, g: 'List[int]', s: 'List[int]') -> 'int':
        g.sort()
        s.sort()
        res = 0
        for child in g:
            while s:
                cookie = s.pop(0)
                if cookie >= child:
                    res += 1
                    break
        return res
