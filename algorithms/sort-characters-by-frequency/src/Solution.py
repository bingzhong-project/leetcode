import collections
import heapq


class Solution:
    def frequencySort(self, s: 'str') -> 'str':
        counter = collections.Counter()
        for string in s:
            counter[string] += 1
        heap = []
        for string, count in counter.items():
            heap.append((count, string))
        heapq.heapify(heap)
        res = ""
        while heap:
            string, count = heapq.heappop(heap)
            res += string * count
        return res[::-1]
