import collections


class Solution:
    def deleteAndEarn(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        counter = collections.Counter(nums)
        array = sorted(list(set(nums)))
        pre_take = 0
        pre_skip = 0
        pre_take = array[0] * counter[array[0]]
        res = pre_take
        for i in range(1, len(array)):
            take = 0
            take = array[i] * counter[array[i]] + (
                pre_skip
                if array[i] - 1 == array[i - 1] else max(pre_take, pre_skip))
            skip = max(pre_take, pre_skip)
            res = max(take, skip)

            pre_take = take
            pre_skip = skip

        return res
