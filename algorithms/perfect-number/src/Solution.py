class Solution:
    def checkPerfectNumber(self, num: 'int') -> 'bool':
        res = 1
        if num == 1:
            return False
        elif num <= 10:
            for i in range(2, num):
                if num % i == 0:
                    res += i
            return res == num
        else:
            for i in [2, 3, 5]:
                n = i
                while num % n == 0:
                    res += n
                    res += num // n
                    n *= i
            return res == num
