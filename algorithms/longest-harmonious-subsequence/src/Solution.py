import collections


class Solution:
    def findLHS(self, nums: 'List[int]') -> 'int':
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
        res = 0
        for num in sorted(list(counter.keys())):
            length = 0
            if num + 1 in counter:
                length = counter[num] + counter[num + 1]
            res = max(length, res)
        return res
