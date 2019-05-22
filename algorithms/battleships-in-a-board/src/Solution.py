class Solution:
    def countBattleships(self, board: 'List[List[str]]') -> 'int':
        def dfs(board, i, j):
            if board[i][j] == '.' or board[i][j] == 'O':
                return
            board[i][j] = 'O'
            if i - 1 >= 0:
                dfs(board, i - 1, j)
            if i + 1 < len(board):
                dfs(board, i + 1, j)
            if j - 1 >= 0:
                dfs(board, i, j - 1)
            if j + 1 < len(board[i]):
                dfs(board, i, j + 1)

        res = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    res += 1
                    dfs(board, i, j)
        return res
