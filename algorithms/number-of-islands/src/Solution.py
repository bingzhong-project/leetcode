class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, visited, i, j):
            if i > len(grid) - 1 or i < 0 or j > len(grid[-1]) - 1 or j < 0:
                return
            if grid[i][j] == '0':
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            dfs(grid, visited, i - 1, j)
            dfs(grid, visited, i + 1, j)
            dfs(grid, visited, i, j - 1)
            dfs(grid, visited, i, j + 1)

        res = 0
        visited = [[False for _ in range(len(grid[-1]))]
                   for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    res += 1

        return res
