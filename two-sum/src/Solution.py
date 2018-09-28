class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return sorted([i, cache[diff]])
            cache[nums[i]] = i
