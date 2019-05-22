class Solution:
    def countBattleships(self, board: 'List[List[str]]') -> 'int':
        res = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if (i - 1 < 0 or board[i - 1][j] == '.') and (
                            j - 1 < 0 or board[i][j - 1] == '.'):
                        res += 1
        return res
