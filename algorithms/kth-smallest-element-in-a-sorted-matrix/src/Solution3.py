class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] <= mid:
                        cnt += 1
                    else:
                        break
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left
