class Solution:
    def canVisitAllRooms(self, rooms: list) -> bool:
        def dfs(adj, node, visited, count):
            count[0] += 1
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(adj, child, visited, count)

        count = [0]
        dfs(rooms, 0, set(), count)

        return count[0] == len(rooms)
