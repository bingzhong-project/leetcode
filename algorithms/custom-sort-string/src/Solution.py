import collections


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        counter = collections.Counter(T)
        res = ""
        for s in S:
            for _ in range(counter[s]):
                res += s
            del counter[s]
        for s, count in counter.items():
            for _ in range(count):
                res += s
        
        return res
