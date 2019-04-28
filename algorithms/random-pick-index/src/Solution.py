import collections
import random


class Solution:
    def __init__(self, nums: 'List[int]'):
        self.map = collections.defaultdict(list)
        for i in range(len(nums)):
            self.map[nums[i]] += [i]

    def pick(self, target: 'int') -> 'int':
        indexes = self.map[target]
        return indexes[random.randint(0, len(indexes) - 1)]
