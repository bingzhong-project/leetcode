class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def dfs(graph, visited, i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for node in graph[i]:
                if not dfs(graph, visited, node):
                    return False
            visited[i] = 1
            return True

        graph = [[] for i in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        for i in range(numCourses):
            if not dfs(graph, visited, i):
                return False
        return True
