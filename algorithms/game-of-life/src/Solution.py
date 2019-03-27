class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """

        INT_MIN = -2**31

        def is_life(num):
            if num == 1 or num == -1:
                return True
            if num == 0 or num == INT_MIN:
                return False

        def around(i, j, row, col):
            res = []
            if i - 1 >= 0:
                res.append((i - 1, j))
            if i + 1 < row:
                res.append((i + 1, j))
            if j - 1 >= 0:
                res.append((i, j - 1))
            if j + 1 < col:
                res.append((i, j + 1))
            if i - 1 >= 0 and j - 1 >= 0:
                res.append((i - 1, j - 1))
            if i - 1 >= 0 and j + 1 < col:
                res.append((i - 1, j + 1))
            if i + 1 < row and j - 1 >= 0:
                res.append((i + 1, j - 1))
            if i + 1 < row and j + 1 < col:
                res.append((i + 1, j + 1))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                pos = around(i, j, len(board), len(board[i]))
                life_count = 0
                for m, n in pos:
                    if is_life(board[m][n]):
                        life_count += 1
                if (life_count < 2 and board[i][j] == 1) or (life_count > 3
                                                             and board[i][j]):
                    board[i][j] = -1
                if life_count == 3 and board[i][j] == 0:
                    board[i][j] = INT_MIN

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == INT_MIN:
                    board[i][j] = 1
