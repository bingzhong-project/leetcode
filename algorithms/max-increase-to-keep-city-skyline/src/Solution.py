class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        row_max = [0 for _ in range(len(grid))]
        col_max = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            row_max[i] = max(grid[i])
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                col_max[j] = max(col_max[j], grid[i][j])
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_change = min(row_max[i], col_max[j])
                res += max_change - grid[i][j]

        return res
