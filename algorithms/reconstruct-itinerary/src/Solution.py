import collections


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def dfs(adj, airport, res):
            while adj[airport]:
                dfs(adj, adj[airport].pop(0), res)
            res.append(airport)

        adj = collections.defaultdict(list)
        for f, t in sorted(tickets):
            adj[f].append(t)
        res = []
        dfs(adj, 'JFK', res)
        return res[::-1]
