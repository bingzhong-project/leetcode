class Solution:
    def convertToBase7(self, num: 'int') -> 'str':
        if num == 0:
            return '0'
        negative = num < 0
        num = abs(num)
        res = ""
        while num != 0:
            div, mod = divmod(num, 7)
            res = str(mod) + res
            num = div
        return "-" + res if negative else res
