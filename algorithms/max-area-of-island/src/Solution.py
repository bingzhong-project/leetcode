class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:
        def move(i, j):
            return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def search(grid, i, j, visited):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1:
                return 0
            if grid[i][j] == 0:
                return 0
            area = 1
            visited.add((i, j))
            for m, n in move(i, j):
                if (m, n) in visited:
                    continue
                area += search(grid, m, n, visited)
            return area

        visited = set()
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visited:
                    continue
                area = max(area, search(grid, i, j, visited))

        return area
