class Solution:
    def addDigits(self, num: 'int') -> 'int':
        if num < 10:
            return num
        else:
            return 1 + (num - 1) % 9
