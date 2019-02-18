class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def dfs(adj, visited, i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for node in adj[i]:
                if not dfs(adj, visited, node):
                    return False
            visited[i] = 1
            return True

        adj = [[] for i in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        for i in range(numCourses):
            if not dfs(adj, visited, i):
                return False
        return True
