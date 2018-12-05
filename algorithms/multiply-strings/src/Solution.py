class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        cache = [[0 for _ in range(len(num1) + len(num2) - 1)]
                 for _ in range(len(num2))]
        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1) - 1, -1, -1):
                n = int(num1[j])
                m = int(num2[i])
                cache[i][i + j] = m * n
        carry = 0
        for j in range(len(cache[-1]) - 1, -1, -1):
            sum = 0
            for i in range(len(cache) - 1, -1, -1):
                sum += cache[i][j]
            sum += carry
            if j == 0:
                result = str(sum) + result
            else:
                div, mod = divmod(sum, 10)
                carry = div
                result = str(mod) + result
        if result[0] == '0':
            return '0'
        else:
            return result
