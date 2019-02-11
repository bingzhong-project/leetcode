class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def neighbors(row, column, row_count, column_count):
            neighbor = []
            for direction in (-1, 0), (1, 0), (0, -1), (0, 1):
                x = row + direction[0]
                y = column + direction[1]
                if x < 0 or y < 0 or x > row_count - 1 or y > column_count - 1:
                    continue
                neighbor.append((x, y))
            return neighbor

        def find_same_island(A, i, j, visited, res):
            for x, y in neighbors(i, j, len(A), len(A[i])):
                if A[x][y] == 0:
                    continue
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                res.append((x, y))
                find_same_island(A, x, y, visited, res)

        def get_island(A, visited, res):
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] == 1 and (i, j) not in visited:
                        visited.add((i, j))
                        res.append((i, j))
                        find_same_island(A, i, j, visited, res)
                        return

        sources = list()
        targets = list()
        visited = set()
        get_island(A, visited, sources)
        get_island(A, visited, targets)

        visited = set(sources)
        targets = set(targets)

        queue = [(node, 0) for node in sources]

        while queue:
            node, distance = queue.pop(0)
            if node in targets:
                return distance - 1
            i, j = node
            for nei in neighbors(i, j, len(A), len(A[i])):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, distance + 1))
