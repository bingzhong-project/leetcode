class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(graph, i):
            if graph[i][i] != 1:
                return
            graph[i][i] = -1
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    dfs(graph, j)

        res = 0
        for i in range(len(M)):
            if M[i][i] == 1:
                res += 1
                dfs(M, i)
        return res
