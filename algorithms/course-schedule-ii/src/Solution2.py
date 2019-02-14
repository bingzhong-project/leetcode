class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for i in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        counter = 0
        res = []

        while queue:
            vertex = queue.pop(0)
            counter += 1
            res.append(vertex)
            for u in adj[vertex]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.append(u)

        return res if counter == numCourses else []
