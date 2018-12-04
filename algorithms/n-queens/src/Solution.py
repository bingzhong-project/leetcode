class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def is_postion_right(positions, queen_no):
            if queen_no == 0:
                return True
            if abs(positions[queen_no] - positions[queen_no - 1]) > 1:
                for i in range(queen_no):
                    if positions[i] == positions[queen_no] or queen_no + positions[queen_no] == i + positions[i] or queen_no - positions[queen_no] == i - positions[i]:
                        return False
                return True
            else:
                return False

        def find_queen_position(queen_count, positions, result, queen_no=0):
            if queen_no == queen_count:
                checkboard = [n * '.' for i in range(n)]
                for i in range(len(positions)):
                    column = positions[i]
                    row = list(checkboard[i])
                    row[column] = 'Q'
                    checkboard[i] = "".join(row)
                result.append(checkboard)
                return
            for i in range(queen_count):
                positions[queen_no] = i
                if is_postion_right(positions, queen_no):
                    find_queen_position(queen_count, positions, result,
                                        queen_no + 1)

        result = []
        find_queen_position(n, [-1 for m in range(n)], result)

        return result
