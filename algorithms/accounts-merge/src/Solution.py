import collections


class Solution:
    def accountsMerge(self, accounts: list) -> list:
        def dfs(adj, accounts, visited, mail, merge):
            if mail in visited:
                return
            merge.append(mail)
            visited.add(mail)
            for i in adj[mail]:
                for j in range(1, len(accounts[i])):
                    dfs(adj, accounts, visited, accounts[i][j], merge)

        adj = collections.defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                adj[mail] += [i]
        res = []
        visited = set()
        for i in range(len(accounts)):
            merge = []
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in visited:
                    continue
                dfs(adj, accounts, visited, accounts[i][j], merge)
            if len(merge) > 0:
                res.append([accounts[i][0]] + sorted(merge))

        return res
