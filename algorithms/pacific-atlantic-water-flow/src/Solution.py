class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        PACIFIC = 1
        ATLANTIC = 0
        NOT = -1
        PACIFIC_ATLANTIC = 10

        def next(i, j):
            return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def dfs(matrix, i, j, visited, cache):
            if (i, j) in cache:
                return cache[(i, j)]
            states = [NOT for _ in range(4)]
            next_pos = next(i, j)
            for n in range(len(next_pos)):
                ni, nj = next_pos[n]
                if ni < 0:
                    states[n] = PACIFIC
                elif ni > len(matrix) - 1:
                    states[n] = ATLANTIC
                elif nj < 0:
                    states[n] = PACIFIC
                elif nj > len(matrix[0]) - 1:
                    states[n] = ATLANTIC
                elif matrix[i][j] >= matrix[ni][nj] and (ni,
                                                         nj) not in visited:
                    visited.add((ni, nj))
                    states[n] = dfs(matrix, ni, nj, visited, cache)
            is_pacific = False
            is_atlantic = False
            for state in states:
                if state == PACIFIC_ATLANTIC:
                    is_pacific = True
                    is_atlantic = True
                elif state == PACIFIC:
                    is_pacific = True
                elif state == ATLANTIC:
                    is_atlantic = True
            if is_pacific and is_atlantic:
                return PACIFIC_ATLANTIC
            elif is_pacific:
                return PACIFIC
            elif is_atlantic:
                return ATLANTIC
            else:
                return NOT

        res = []
        cache = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                visited = set()
                visited.add((i, j))
                state = dfs(matrix, i, j, visited, cache)
                cache[(i, j)] = state
                if state == PACIFIC_ATLANTIC:
                    res.append([i, j])

        return res
