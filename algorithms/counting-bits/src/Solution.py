class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for _ in range(num + 1)]
        for n in range(num + 1):
            if n == 0:
                res[n] = 0
            else:
                if n % 2 == 0:
                    res[n] = res[n // 2]
                else:
                    res[n] = res[n - 1] + 1
        return res
