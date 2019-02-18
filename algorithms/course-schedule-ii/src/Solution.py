class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def dfs(adj, visited, topology_list, i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for node in adj[i]:
                if not dfs(adj, visited, topology_list, node):
                    return False
            visited[i] = 1
            topology_list.append(i)
            return True

        adj = [[] for i in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        topology_list = []
        for i in range(numCourses):
            if not dfs(adj, visited, topology_list, i):
                return []
        return topology_list[::-1]
