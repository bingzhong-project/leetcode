class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_steal = [0 for _ in range(len(nums))]
        max_not_steal = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                max_steal[i] = nums[i]
                max_not_steal[i] = 0
            else:
                max_steal[i] = max_not_steal[i - 1] + nums[i]
                max_not_steal[i] = max(max_steal[i - 1], max_not_steal[i - 1])
        return max(max_steal[-1], max_not_steal[-1])
