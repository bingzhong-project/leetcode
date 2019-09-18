class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = []
        n = N
        while n > 0:
            div, mod = divmod(n, 10)
            digits.append(mod)
            n = div

        boundary = -1
        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                boundary = i
                digits[i + 1] -= 1
        for i in range(boundary + 1):
            digits[i] = 9

        res = digits[-1]
        for i in range(len(digits) - 2, -1, -1):
            res = res * 10 + digits[i]
        return res
