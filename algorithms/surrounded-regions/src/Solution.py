class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def dfs(board, visited, positions, i, j):
            if i > len(board) - 1 or i < 0 or j > len(board[-1]) - 1 or j < 0:
                return True
            if board[i][j] == 'X':
                return False
            if visited[i][j]:
                return False
            visited[i][j] = True
            positions.append([i, j])
            return dfs(board, visited, positions, i - 1, j) or dfs(
                board, visited, positions, i + 1, j) or dfs(
                    board, visited, positions, i, j - 1) or dfs(
                        board, visited, positions, i, j + 1)

        visited = [[False for _ in range(len(board[-1]))]
                   for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[-1])):
                if board[i][j] == 'O' and not visited[i][j]:
                    positions = list()
                    flag = dfs(board, visited, positions, i, j)
                    if not flag:
                        for pos in positions:
                            board[pos[0]][pos[1]] = 'X'
