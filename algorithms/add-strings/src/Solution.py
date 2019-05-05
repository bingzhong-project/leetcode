class Solution:
    def addStrings(self, num1: 'str', num2: 'str') -> 'str':
        if len(num1) < len(num2):
            temp = num1
            num1 = num2
            num2 = temp
        i = 1
        carry = 0
        res = ''
        while len(num1) - i >= 0:
            add1 = int(num1[len(num1) - i])
            add2 = int(num2[len(num2) - i]) if len(num2) - i >= 0 else 0
            ans = add1 + add2 + carry
            if ans > 9:
                carry = 1
                ans %= 10
            else:
                carry = 0
            i += 1
            res = str(ans) + res
        if carry > 0:
            res = str(carry) + res
        return res
