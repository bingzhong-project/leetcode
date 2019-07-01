import collections


class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        table = collections.Counter()
        table[0] = 1
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in table:
                res += table[s - k]
            table[s] += 1
        return res
