import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        heap = []
        for string, count in counter.items():
            heapq.heappush(heap, (-count, string))
        res = ""
        while heap:
            count, string = heapq.heappop(heap)
            count = -count
            if len(res) == 0 or res[-1] != string:
                res += string
                count -= 1
                if count > 0:
                    heapq.heappush(heap, (-count, string))
            else:
                if not heap:
                    return ""
                second_count, second_string = heapq.heappop(heap)
                second_count = -second_count
                res += second_string
                second_count -= 1
                if second_count > 0:
                    heapq.heappush(heap, (-second_count, second_string))
                heapq.heappush(heap, (-count, string))

        return res
