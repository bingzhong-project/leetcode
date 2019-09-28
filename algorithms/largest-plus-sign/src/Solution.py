class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: list) -> int:
        mines_set = {tuple(mine) for mine in mines}
        dp = [[0 for _ in range(N)] for _ in range(N)]
        res = 0
        for j in range(N):
            cnt = 0
            for i in range(N):
                cnt = 0 if (i, j) in mines_set else cnt + 1
                dp[i][j] = cnt
            cnt = 0
            for i in range(N - 1, -1, -1):
                cnt = 0 if (i, j) in mines_set else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)

        for i in range(N):
            cnt = 0
            for j in range(N):
                cnt = 0 if (i, j) in mines_set else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for j in range(N - 1, -1, -1):
                cnt = 0 if (i, j) in mines_set else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
                res = max(dp[i][j], res)

        return res
