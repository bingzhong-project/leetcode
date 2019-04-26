import sys


class Solution:
    def maxRotateFunction(self, A: 'List[int]') -> 'int':
        """两个循环，时间复杂度 O(n²) TLE

        Returns:
            int: 结果
        """
        if len(A) == 0:
            return 0
        res = -sys.maxsize
        for i in range(len(A)):
            sum = 0
            for j in range(len(A)):
                num = (len(A) + (j - i)) % len(A)
                sum += num * A[j]
            res = max(res, sum)
        return res
