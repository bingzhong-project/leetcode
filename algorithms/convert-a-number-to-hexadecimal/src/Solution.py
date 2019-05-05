class Solution:
    def toHex(self, num: 'int') -> 'str':
        HEX = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
            'd', 'e', 'f'
        ]
        if num == 0:
            return '0'
        res = ''
        times = 0
        while num and times < 8:
            res = HEX[num & 15] + res
            num = (num >> 4)
            times += 1
        return res
