class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def func(nums, index, target, cache):
            if index == len(nums):
                return 1 if target == 0 else 0
            if (index, target) in cache:
                return cache[(index, target)]
            ans1 = func(nums, index + 1, target + nums[index], cache)
            ans2 = func(nums, index + 1, target - nums[index], cache)

            res = ans1 + ans2
            cache[(index, target)] = res
            return res

        return func(nums, 0, S, {})
