class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        res = 1
        for i in range(1, len(nums)):
            max_length = 0
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    max_length = max(max_length, dp[j])
            dp[i] = max_length + 1
            res = max(res, dp[i])
        return res
