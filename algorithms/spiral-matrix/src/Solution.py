class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[left][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res
