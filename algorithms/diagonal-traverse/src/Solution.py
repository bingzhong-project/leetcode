class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if len(matrix) == 0:
            return []
        UP = 1
        DOWN = -1
        res = []
        row = len(matrix)
        col = len(matrix[0])
        total = row * col
        i = 0
        j = 0
        direction = UP
        while len(res) < total:
            res.append(matrix[i][j])
            if direction == UP:
                while i - 1 >= 0 and j + 1 < col:
                    i -= 1
                    j += 1
                    res.append(matrix[i][j])
                if j + 1 >= col:
                    i += 1
                else:
                    j += 1
                direction = DOWN
            else:
                while i + 1 < row and j - 1 >= 0:
                    i += 1
                    j -= 1
                    res.append(matrix[i][j])
                if i + 1 >= row:
                    j += 1
                else:
                    i += 1
                direction = UP
        return res
