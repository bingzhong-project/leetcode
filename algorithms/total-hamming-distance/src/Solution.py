import collections


class Solution:
    def totalHammingDistance(self, nums: 'List[int]') -> 'int':
        ones = collections.Counter()
        for num in nums:
            i = 0
            while num:
                if num & 1:
                    ones[i] += 1
                i += 1
                num >>= 1
        res = 0
        for _, one in ones.items():
            res += one * (len(nums) - one)

        return res
