class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        total = [0 for _ in range(len(triangle[-1]) + 1)]
        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i])):
                total[j] = triangle[i][j] + min(total[j], total[j + 1])
        return total[0]
