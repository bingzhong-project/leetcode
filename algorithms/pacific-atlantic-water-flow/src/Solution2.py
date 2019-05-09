class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(matrix)
        column = len(matrix[0]) if row != 0 else 0

        def next(i, j):
            return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def dfs(matrix, i, j, visited):
            visited[i][j] = True
            for ni, nj in next(i, j):
                if ni >= 0 and ni < row and nj >= 0 and nj < column and matrix[ni][nj] >= matrix[i][j] and not visited[ni][nj]:
                    dfs(matrix, ni, nj, visited)

        pacific_visitied = [[False for _ in range(column)] for _ in range(row)]
        atlantic_visitied = [[False for _ in range(column)]
                             for _ in range(row)]
        for i in range(row):
            dfs(matrix, i, 0, pacific_visitied)
            dfs(matrix, i, column - 1, atlantic_visitied)
        for j in range(column):
            dfs(matrix, 0, j, pacific_visitied)
            dfs(matrix, row - 1, j, atlantic_visitied)

        res = []
        for i in range(row):
            for j in range(column):
                if pacific_visitied[i][j] and atlantic_visitied[i][j]:
                    res.append([i, j])
        return res
