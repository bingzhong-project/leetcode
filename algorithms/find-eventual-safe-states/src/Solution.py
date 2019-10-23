class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        BLACK = 1
        WHITE = 0
        GRAY = -1

        def dfs(adj, node, color):
            if color[node] == GRAY:
                return False
            if color[node] == BLACK:
                return True
            color[node] = GRAY
            for child in adj[node]:
                if not dfs(adj, child, color):
                    return False
            color[node] = BLACK
            return True

        color = [WHITE for _ in range(len(graph))]
        for node in range(len(graph)):
            if color[node] == WHITE:
                dfs(graph, node, color)

        res = []
        for node in range(len(graph)):
            if color[node] != GRAY:
                res.append(node)
        return res
