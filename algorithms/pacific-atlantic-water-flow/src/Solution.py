class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def pacific(i, j):
            return [(i - 1, j), (i, j - 1)]

        def atlantic(i, j):
            return [(i + 1, j), (i, j + 1)]

        def dfs(matrix, i, j, visited):
            pass

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                visited = set()
                visited.add((i, j))
                pass

        return res


if __name__ == "__main__":
    print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4],
                                      [2, 4, 5, 3, 1], [6, 7, 1, 4,
                                                        5], [5, 1, 1, 2, 4]]))
