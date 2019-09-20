import heapq


class Solution:
    def networkDelayTime(self, times: list, N: int, K: int) -> int:
        INF = 2**31
        adj = [[] for _ in range(N + 1)]
        distance = [INF for _ in range(N + 1)]
        distance[0] = -1
        for time in times:
            adj[time[0]].append((time[2], time[1]))
        distance[K] = 0
        queue = []
        queue.append((0, K))
        visited = set()
        while queue:
            _, u = heapq.heappop(queue)
            visited.add(u)
            for uv, v in adj[u]:
                if v in visited:
                    continue
                if distance[v] > distance[u] + uv:
                    distance[v] = distance[u] + uv
                    heapq.heappush(queue, (distance[v], v))

        max_distance = max(distance)

        return max_distance if max_distance != INF else -1
