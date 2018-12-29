class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def dfs(graph, visited, topology_list, i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for node in graph[i]:
                if not dfs(graph, visited, topology_list, node):
                    return False
            visited[i] = 1
            topology_list.append(i)
            return True

        graph = [[] for i in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        topology_list = []
        for i in range(numCourses):
            if not dfs(graph, visited, topology_list, i):
                return []
        return topology_list[::-1]
