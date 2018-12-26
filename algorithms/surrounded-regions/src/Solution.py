class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def dfs(board, i, j):
            if i > len(board) - 1 or i < 0 or j > len(board[-1]) - 1 or j < 0:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = '$'
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)

        for i in range(len(board)):
            for j in range(len(board[-1])):
                if (i == 0 or i == len(board) - 1 or j == 0
                        or j == len(board[i]) - 1) and board[i][j] == 'O':
                    dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '$':
                    board[i][j] = 'O'
