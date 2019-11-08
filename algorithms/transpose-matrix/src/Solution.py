class Solution:
    def transpose(self, A: list) -> list:
        row = len(A)
        column = len(A[0])

        res = [[0 for _ in range(row)] for _ in range(column)]
        for j in range(column):
            for i in range(row):
                res[j][i] = A[i][j]

        return res
