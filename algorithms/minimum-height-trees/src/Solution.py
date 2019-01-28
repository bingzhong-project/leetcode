class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # 该解法 TLE

        def calculate_height(adj, root):
            height = {}
            height[root] = 0

            visited = [False for _ in range(len(adj))]
            visited[root] = True

            queue = []
            queue.append(root)
            while len(queue) > 0:
                node = queue.pop(0)
                for i in range(len(adj[node])):
                    child_node = adj[node][i]
                    if not visited[child_node]:
                        visited[child_node] = True
                        height[child_node] = height[node] + 1
                        queue.append(child_node)
            return max(height.values())

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        min_height = 2**31
        res = []
        for i in range(n):
            height = calculate_height(adj, i)
            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)
        return res
