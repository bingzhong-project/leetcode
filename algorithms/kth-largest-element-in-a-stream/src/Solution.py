import heapq


class KthLargest:
    def __init__(self, k: int, nums: list):
        self.heap = []
        self.size = k
        for num in nums:
            if len(self.heap) < self.size:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heapreplace(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
