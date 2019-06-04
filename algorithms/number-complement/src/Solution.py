class Solution:
    def findComplement(self, num: 'int') -> 'int':
        n = 1
        factor = 2
        while n < num:
            n += factor
            factor *= 2
        return n ^ num
