class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) == 0:
            return [0]

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        leaves = []
        for vertex in range(n):
            if len(adj[vertex]) == 1:
                leaves.append(vertex)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if (len(adj[j]) == 1):
                    new_leaves.append(j)
            leaves = new_leaves

        return leaves
