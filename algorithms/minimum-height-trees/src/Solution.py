class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # 该解法 TLE

        def calculate_height(graph, root):
            height = {}
            height[root] = 0

            visited = [False for _ in range(len(graph))]
            visited[root] = True

            queue = []
            queue.append(graph[root][0])
            while len(queue) > 0:
                node = queue.pop(0)
                for i in range(1, len(graph[node])):
                    child_node = graph[node][i]
                    if not visited[child_node]:
                        visited[child_node] = True
                        height[child_node] = height[node] + 1
                        queue.append(child_node)
            return max(height.values())

        graph = [[i] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        min_height = 2**31
        res = []
        for i in range(n):
            height = calculate_height(graph, i)
            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)
        return res
