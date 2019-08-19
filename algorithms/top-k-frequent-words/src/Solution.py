import heapq
import collections


class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        counter = collections.Counter()
        for word in words:
            counter[word] += 1
        heap = []
        for word, count in counter.items():
            heapq.heappush(heap, (-count, word))
        res = []
        i = 0
        while i < k:
            count, word = heapq.heappop(heap)
            res.append(word)
            i += 1
        return res
