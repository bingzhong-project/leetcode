class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        res = -2**31
        max_cache = 0
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                max_cache = num
            else:
                max_cache = max(max_cache + num, num)
            res = max(res, max_cache)
        return res
