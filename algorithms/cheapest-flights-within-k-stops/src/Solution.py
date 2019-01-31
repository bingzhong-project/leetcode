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

        res = 2**31
        queue = []
        queue.append((src, 0))
        layer = -1

        while len(queue) > 0:
            layer += 1
            if layer > K + 1:
                break
            for _ in range(len(queue)):
                city, price = queue.pop(0)
                if city == dst:
                    res = min(res, price)
                for next_city, next_price in adj[city]:
                    if next_price + price > res:
                        continue
                    queue.append((next_city, next_price + price))

        return res if res != 2**31 else -1
