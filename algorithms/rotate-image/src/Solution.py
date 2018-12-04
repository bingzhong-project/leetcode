class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        up = 0
        down = len(matrix) - 1
        while up < down:
            up_row = matrix[up]
            down_row = matrix[down]
            matrix[up] = down_row
            matrix[down] = up_row
            up += 1
            down -= 1
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if i != j and i < j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
