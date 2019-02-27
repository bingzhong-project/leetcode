class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        def position(cursor, col):
            return divmod(cursor, col)

        if len(matrix) == 0:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1

        while left <= right:
            mid = (left + right) // 2
            i, j = position(mid, col)
            if matrix[i][j] > target:
                right = mid - 1
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                return True

        return False
