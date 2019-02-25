class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        positions = {}
        box = {}
        box[0] = box[1] = box[2] = 0
        box[3] = box[4] = box[5] = 1
        box[6] = box[7] = box[8] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] not in positions:
                        positions[board[i][j]] = [(i, j)]
                    else:
                        for row, column in positions[board[i][j]]:
                            if row == i:
                                return False
                            if column == j:
                                return False
                            if box[row] == box[i] and box[column] == box[j]:
                                return False
                        positions[board[i][j]].append((i, j))

        return True
