class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_steal = 0
        max_not_steal = 0
        for i in range(len(nums)):
            if i == 0:
                max_steal = nums[i]
                max_not_steal = 0
            else:
                temp = max_steal
                max_steal = max_not_steal + nums[i]
                max_not_steal = max(temp, max_not_steal)
        return max(max_steal, max_not_steal)
