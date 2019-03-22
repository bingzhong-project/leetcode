class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def binary(matrix, row, pos, target, i, j):
            if i > j:
                return False
            mid = (i + j) // 2
            val = matrix[pos][mid] if row else matrix[mid][pos]
            if val > target:
                return binary(matrix, row, pos, target, i, mid - 1)
            elif val < target:
                return binary(matrix, row, pos, target, mid + 1, j)
            else:
                return True

        if len(matrix) == 0:
            return False

        left, top = 0, 0
        right, bot = len(matrix[0]) - 1, len(matrix) - 1
        while left <= right and top <= bot:
            if binary(matrix, True, top, target, left, right):
                return True
            else:
                top += 1
            if binary(matrix, False, left, target, top, bot):
                return True
            else:
                left += 1
        return False
