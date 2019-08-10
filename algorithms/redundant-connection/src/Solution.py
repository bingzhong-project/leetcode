class Solution:
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        def topology(adj, color, u, pre):
            if color[u] == BLACK:
                return True
            if color[u] == GRAY:
                return False
            color[u] = GRAY
            for v in adj[u]:
                if pre == v:
                    continue
                if not topology(adj, color, v, u):
                    return False
            color[u] = BLACK
            return True

        WHITE = 0
        GRAY = -1
        BLACK = 1
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in tuple(edges):
            adj[u].append(v)
            adj[v].append(u)
            color = [WHITE for _ in range(len(edges) + 1)]
            if not topology(adj, color, u, None):
                return [u, v]
