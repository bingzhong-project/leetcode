class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    for x in range(len(matrix[i])):
                        matrix[i][x] = 0 if matrix[i][x] == 0 else None
                    for x in range(len(matrix)):
                        matrix[x][j] = 0 if matrix[x][j] == 0 else None

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0 if matrix[i][j] is None else matrix[i][j]
