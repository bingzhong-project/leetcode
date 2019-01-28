class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        INT_MAX = 2**31

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        row_len = len(matrix)
        column_len = len(matrix[0])
        queue = []
        for i in range(row_len):
            for j in range(column_len):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = INT_MAX

        while len(queue) > 0:
            i, j = queue.pop(0)
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]
                if x < 0 or y < 0 or x > row_len - 1 or y > column_len - 1 or matrix[x][y] <= matrix[i][j] + 1:
                    continue
                matrix[x][y] = matrix[i][j] + 1
                queue.append((x, y))

        return matrix
