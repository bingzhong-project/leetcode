class Solution:
    def getRow(self, rowIndex: int) -> list:
        res = [1 for _ in range(rowIndex + 1)]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]

        return res
