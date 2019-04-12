import heapq


class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 1:
            val, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            k -= 1
        return heapq.heappop(heap)[0]
