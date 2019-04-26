class Solution:
    def maxRotateFunction(self, A: 'List[int]') -> 'int':
        """计算公式： F(i) = F(i-1) + sum - n*A[n-i]

        Returns:
            int: 结果
        """
        if len(A) == 0:
            return 0
        length = len(A)
        F = [0 for _ in range(length)]
        s = sum(A)
        for i in range(length):
            F[0] += i * A[i]
        for i in range(1, length):
            F[i] = F[i - 1] + s - length * A[length - i]
        return max(F)
