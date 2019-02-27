class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        num = 1
        while True:
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return matrix
