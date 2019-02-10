class Solution:
    def isBipartite(self, graph: 'List[List[int]]') -> 'bool':
        color = [0 for _ in range(len(graph))]

        for root in range(len(graph)):
            if color[root] != 0:
                continue
            queue = []
            queue.append(root)
            color[root] = 1
            while queue:
                v = queue.pop(0)
                for u in graph[v]:
                    if color[u] == 0:
                        color[u] = -color[v]
                        queue.append(u)
                    else:
                        if color[v] == color[u]:
                            return False
        return True
