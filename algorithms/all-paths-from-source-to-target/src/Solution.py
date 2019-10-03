class Solution:
    def allPathsSourceTarget(self, graph: list) -> list:
        def dfs(adj, node):
            if len(adj[node]) == 0:
                return [[node]]
            paths = []
            for child in adj[node]:
                for path in dfs(adj, child):
                    paths.append([node] + path)

            return paths

        return dfs(graph, 0)
