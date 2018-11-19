class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        total = [[0 for _ in range(len(triangle[-1]))]
                 for _ in range(len(triangle))]
        res = 0
        for i in range(len(triangle)):
            min_sum = 2**31
            for j in range(len(triangle[i])):
                pre_row = 0 if i == 0 else i - 1
                pre_column = 0 if j == 0 else j - 1
                if j == len(triangle[i]) - 1:
                    total[i][j] = triangle[i][j] + total[pre_row][pre_column]
                else:
                    total[i][j] = triangle[i][j] + min(
                        total[pre_row][j], total[pre_row][pre_column])
                min_sum = min(min_sum, total[i][j])
                res = min_sum
        return res
