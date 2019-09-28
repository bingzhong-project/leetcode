import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = collections.Counter(S)
        res = 0
        for j in J:
            res += counter[j]
        
        return res
