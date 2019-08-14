class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            max_length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_length = max(max_length, dp[j])
            dp[i] = max_length + 1
            res = max(res, dp[i])
        return res
