class Solution:
    def generate(self, numRows: int) -> list:
        res = [None for _ in range(numRows)]
        for i in range(numRows):
            res[i] = [1 for _ in range(i + 1)]
            for j in range(i):
                if j < len(res[i]) and j - 1 >= 0:
                    res[i][j] = res[i - 1][j] + res[i - 1][j - 1]

        return res
