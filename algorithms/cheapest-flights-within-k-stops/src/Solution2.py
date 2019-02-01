import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        pq = [(0, -1, src)]
        visited = {src}

        while pq:
            price, stops, city = heapq.heappop(pq)
            if city == dst:
                return price
            visited.add(city)
            for next_city, next_price in adj[city]:
                if next_city not in visited and stops + 1 <= K:
                    heapq.heappush(pq,
                                   (price + next_price, stops + 1, next_city))

        return -1
